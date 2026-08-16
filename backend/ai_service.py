import json
import re

from config import AZURE_OPENAI_API_KEY, AZURE_OPENAI_DEPLOYMENT, AZURE_OPENAI_ENDPOINT
from backend.prompts import ACTION_PROMPT, DECISION_PROMPT, SUMMARY_PROMPT
from backend.text_analysis import clean_transcript, extract_action_items, extract_decisions, extract_topics, split_sentences


try:
    from openai import AzureOpenAI
except ImportError:  # pragma: no cover
    AzureOpenAI = None


def _fallback_summary(transcript: str, topics: list[str]) -> str:
    text = clean_transcript(transcript)
    if not text:
        return "No transcript was provided. Please add a meeting discussion to generate a summary."

    topic_text = ", ".join(topics[:3]) if topics else "project progress"
    return (
        f"The team discussed {topic_text} and aligned on the most urgent priorities for the next phase. "
        "Key workstreams were clarified, responsibilities were mapped to contributors, and the group focused on "
        "timely execution and measurable next steps."
    )


def _llm_client():
    if not AZURE_OPENAI_API_KEY or not AZURE_OPENAI_ENDPOINT or not AZURE_OPENAI_DEPLOYMENT:
        return None
    if AzureOpenAI is None:
        return None
    return AzureOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_version="2024-02-01",
    )


def _call_openai(prompt: str, transcript: str):
    client = _llm_client()
    if client is None:
        return None

    try:
        response = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": transcript},
            ],
            temperature=0.3,
            max_tokens=500,
        )
        return response.choices[0].message.content
    except Exception:
        return None


def _extract_summary(transcript: str, topics: list[str]) -> str:
    llm_content = _call_openai(SUMMARY_PROMPT, transcript)
    if llm_content:
        return llm_content.strip().strip('"')
    return _fallback_summary(transcript, topics)


def _extract_decisions(transcript: str) -> list[str]:
    llm_content = _call_openai(DECISION_PROMPT, transcript)
    if llm_content:
        try:
            parsed = json.loads(llm_content)
            if isinstance(parsed, list) and parsed:
                return [str(item).strip() for item in parsed]
        except Exception:
            pass

    return extract_decisions(transcript)


def _extract_actions(transcript: str) -> list[list[str]]:
    llm_content = _call_openai(ACTION_PROMPT, transcript)
    if llm_content:
        try:
            parsed = json.loads(llm_content)
            if isinstance(parsed, list) and parsed:
                result = []
                for item in parsed:
                    if isinstance(item, dict):
                        result.append([
                            str(item.get("task", "Follow up on discussion")).strip(),
                            str(item.get("owner", "Unassigned")).strip() or "Unassigned",
                            str(item.get("deadline", "Next update")).strip() or "Next update",
                        ])
                if result:
                    return result
        except Exception:
            pass

    return extract_action_items(transcript)


def analyze_meeting(transcript: str) -> dict:
    cleaned = clean_transcript(transcript)
    if not cleaned:
        return {
            "summary": "No transcript was provided. Please enter text or upload a meeting file.",
            "decisions": [],
            "action_items": [],
            "topics": [],
            "word_count": 0,
        }

    topics = extract_topics(cleaned)
    summary = _extract_summary(cleaned, topics)
    decisions = _extract_decisions(cleaned)
    action_items = _extract_actions(cleaned)

    return {
        "summary": summary,
        "decisions": decisions,
        "action_items": action_items,
        "topics": topics,
        "word_count": len(cleaned.split()),
    }


__all__ = ["analyze_meeting"]

