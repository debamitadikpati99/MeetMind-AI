import re
from typing import List


STOPWORDS = {
    "the", "a", "an", "and", "or", "for", "with", "from", "to", "of", "in", "on",
    "at", "by", "as", "is", "was", "were", "we", "they", "he", "she", "it", "this",
    "that", "are", "be", "will", "our", "their", "his", "her", "team", "meeting"
}


def clean_transcript(text: str) -> str:
    if not text:
        return ""
    return re.sub(r"\s+", " ", text).strip()


def split_sentences(text: str) -> List[str]:
    return [sentence.strip() for sentence in re.split(r"(?<=[.!?])\s+", text) if sentence.strip()]


def infer_deadline(sentence: str) -> str:
    lower = sentence.lower()
    if "tomorrow" in lower:
        return "Tomorrow"
    if "friday" in lower:
        return "Friday"
    if "monday" in lower:
        return "Monday"
    if "before review" in lower or "before the review" in lower:
        return "Before review"
    if re.search(r"\bby\s+\w+\s+\d{1,2}\b", lower):
        return "By date"
    if "next meeting" in lower:
        return "Next meeting"
    return "Next update"


def infer_owner(sentence: str) -> str:
    matches = re.findall(r"\b[A-Z][a-z]+\b", sentence)
    owners = [name for name in matches if name.lower() not in {"The", "We", "It", "This", "That"}]
    return owners[0] if owners else "Unassigned"


def extract_topics(text: str) -> List[str]:
    keywords = {
        "Project Updates": ["project", "progress", "timeline", "status", "roadmap"],
        "Design": ["design", "ui", "mockup", "prototype", "wireframe"],
        "Testing": ["test", "qa", "debug", "bug", "validation"],
        "Delivery": ["deadline", "launch", "submission", "handoff", "release"],
        "Collaboration": ["team", "roles", "handover", "review", "feedback"],
    }

    lower = clean_transcript(text).lower()
    topics = [label for label, terms in keywords.items() if any(term in lower for term in terms)]
    return topics[:4] if topics else ["Project Updates", "Action Items", "Risks", "Next Steps"]


def extract_decisions(text: str) -> List[str]:
    sentences = split_sentences(clean_transcript(text))
    decisions = []
    decision_markers = ["decided", "agreed", "approved", "confirmed", "will", "must", "need to", "should"]

    for sentence in sentences:
        lower = sentence.lower()
        if any(marker in lower for marker in decision_markers):
            if len(sentence) > 12 and not re.search(r"\b(will|need to|must|should)\b.*\b(prepare|review|test|fix|update)\b", lower):
                decisions.append(sentence)

    if not decisions:
        for sentence in sentences:
            if len(sentence) > 15:
                decisions.append(sentence)

    return decisions[:4]


def extract_action_items(text: str) -> List[List[str]]:
    sentences = split_sentences(clean_transcript(text))
    action_items = []
    action_markers = ["will", "must", "need to", "should", "can", "going to", "assigned to"]

    for sentence in sentences:
        lower = sentence.lower()
        if any(marker in lower for marker in action_markers):
            owner = infer_owner(sentence)
            deadline = infer_deadline(sentence)
            action_items.append([sentence, owner, deadline])

    if not action_items:
        for sentence in sentences[:3]:
            action_items.append([sentence, "Unassigned", "Next update"])

    return action_items[:5]

