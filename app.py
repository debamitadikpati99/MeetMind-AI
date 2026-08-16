import streamlit as st
from pathlib import Path

from backend.ai_service import analyze_meeting

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="MeetMind AI",
    page_icon="🧠",
    layout="wide",
)

# ---------------- CUSTOM CSS ----------------
st.markdown(
    """
    <style>
    :root {
        --bg: #07111f;
        --panel: #0f172a;
        --panel-soft: #111827;
        --line: rgba(148, 163, 184, 0.24);
        --text: #e2e8f0;
        --muted: #94a3b8;
        --primary: #8b5cf6;
        --primary-soft: rgba(139, 92, 246, 0.18);
        --accent: #38bdf8;
        --success: #34d399;
    }

    .stApp {
        background: linear-gradient(180deg, #020817 0%, #0b1120 40%, #111827 100%);
        color: var(--text);
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .app-shell {
        background: rgba(15, 23, 42, 0.72);
        border: 1px solid var(--line);
        border-radius: 24px;
        padding: 1.5rem;
        box-shadow: 0 18px 50px rgba(15, 23, 42, 0.35);
    }

    .hero {
        margin-bottom: 1rem;
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        letter-spacing: -0.05em;
        margin-bottom: 0.25rem;
    }

    .subtitle {
        font-size: 18px;
        color: #dbeafe;
        font-weight: 600;
    }

    .tagline {
        color: var(--muted);
        font-size: 15px;
        margin-top: 0.3rem;
        max-width: 760px;
    }

    .feature-pill {
        display: inline-block;
        padding: 0.45rem 0.8rem;
        border: 1px solid rgba(56, 189, 248, 0.4);
        background: rgba(56, 189, 248, 0.08);
        color: #bae6fd;
        border-radius: 999px;
        font-size: 12px;
        margin: 0.25rem 0.45rem 0.25rem 0;
        font-weight: 600;
    }

    .section-title {
        font-size: 24px;
        font-weight: 700;
        padding-top: 0.25rem;
        margin-bottom: 0.8rem;
    }

    .metric-card {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.16), rgba(59, 130, 246, 0.08));
        border: 1px solid rgba(167, 139, 250, 0.36);
        border-radius: 18px;
        padding: 1rem 1.15rem;
        height: 100%;
    }

    .metric-label {
        font-size: 12px;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #cbd5e1;
    }

    .metric-value {
        font-size: 30px;
        font-weight: 800;
        margin-top: 0.4rem;
    }

    .info-card {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid var(--line);
        border-radius: 16px;
        padding: 1rem 1.1rem;
        margin-bottom: 1rem;
        color: #e2e8f0;
        line-height: 1.65;
    }

    .pill {
        display: inline-block;
        padding: 0.42rem 0.75rem;
        border-radius: 999px;
        background: rgba(139, 92, 246, 0.12);
        border: 1px solid rgba(167, 139, 250, 0.35);
        color: #ddd6fe;
        margin: 0.2rem 0.35rem 0.15rem 0;
        font-size: 12px;
        font-weight: 600;
    }

    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
    }

    div[data-testid="stSidebar"] {
        background: rgba(2, 6, 23, 0.95);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def load_sample_transcript(name: str) -> str:
    sample_path = Path(__file__).resolve().parent / "sample_data" / f"{name}.txt"
    return sample_path.read_text(encoding="utf-8") if sample_path.exists() else ""


def extract_topics(text: str):
    keywords = {
        "Project Updates": ["project", "progress", "timeline", "status"],
        "Design": ["design", "ui", "wireframe", "prototype"],
        "Testing": ["test", "qa", "debug", "bug"],
        "Delivery": ["deadline", "launch", "submission", "handoff"],
        "Collaboration": ["team", "roles", "handover", "review"],
    }

    lower = text.lower()
    topics = [label for label, terms in keywords.items() if any(term in lower for term in terms)]
    return topics[:4] if topics else ["Project Updates", "Action Items", "Risks", "Next Steps"]


def build_analysis(text: str):
    cleaned = text.strip()
    word_count = len(cleaned.split()) if cleaned else 0
    summary = (
        "The team aligned on top priorities, clarified ownership across key deliverables, and agreed on the "
        "critical checkpoints needed to move the project forward. The discussion centered on execution risk, "
        "quality validation, and timely delivery."
    )
    decisions = [
        "Implementation milestones will be finalized before the next review cycle.",
        "Ownership will follow each team member's strongest area to maintain momentum.",
        "Testing and validation must be completed before the final delivery checkpoint.",
    ]
    action_items = [
        ["Finalize feature scope", "Aisha", "Today"],
        ["Prepare demo walkthrough", "Daniel", "Tomorrow"],
        ["Run QA and edge-case validation", "Nina", "Before review"],
    ]
    return {
        "word_count": word_count,
        "summary": summary,
        "decisions": decisions,
        "action_items": action_items,
        "topics": extract_topics(cleaned),
    }


with st.container():
    st.markdown('<div class="app-shell">', unsafe_allow_html=True)
    st.markdown('<div class="hero">', unsafe_allow_html=True)
    st.markdown('<div class="main-title">🧠 MeetMind AI</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">AI-Powered Meeting Intelligence & Action Item Generator</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="tagline">Turn meeting discussions into clear summaries, decisions, owners, deadlines, and practical next steps.</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div><span class='feature-pill'>Meeting Summary</span><span class='feature-pill'>Key Decisions</span><span class='feature-pill'>Action Items</span><span class='feature-pill'>Topic Detection</span></div>",
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("### Workspace")
        st.caption("Upload a transcript or load a sample.")

        sample_options = ["team_meeting", "project_meeting", "hackathon_meeting"]
        selected_sample = st.selectbox("Sample transcript", sample_options)

        if st.button("Load sample", use_container_width=True):
            st.session_state["manual_text"] = load_sample_transcript(selected_sample)

        st.markdown("---")
        st.markdown("### Included insights")
        st.markdown("- Summary generation")
        st.markdown("- Decision extraction")
        st.markdown("- Responsible owners")
        st.markdown("- Due dates and deadlines")
        st.markdown("- Topic grouping")

    st.markdown('<div class="section-title">📋 Meeting transcript</div>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload a transcript (.txt)", type=["txt"], label_visibility="collapsed")

    if uploaded_file is not None:
        meeting_text = uploaded_file.read().decode("utf-8")
    else:
        meeting_text = st.session_state.get("manual_text", "")

    meeting_text = st.text_area(
        "Paste a meeting transcript",
        value=meeting_text,
        height=240,
        placeholder="Example: We reviewed product progress, assigned follow-ups, and confirmed the final delivery deadline...",
    )

    analyze_col, _ = st.columns([3, 1])
    with analyze_col:
        analyze = st.button("✨ Analyze meeting", use_container_width=True)

    if analyze:
        if meeting_text.strip():
            st.success("Transcript captured. Meeting intelligence is ready.")
            analysis = analyze_meeting(meeting_text)

            st.markdown('<div class="section-title">📊 Meeting overview</div>', unsafe_allow_html=True)
            metric_cols = st.columns(3)
            with metric_cols[0]:
                st.markdown(
                    f'<div class="metric-card"><div class="metric-label">Words</div><div class="metric-value">{analysis["word_count"]}</div></div>',
                    unsafe_allow_html=True,
                )
            with metric_cols[1]:
                st.markdown(
                    f'<div class="metric-card"><div class="metric-label">Decisions</div><div class="metric-value">{len(analysis["decisions"])}</div></div>',
                    unsafe_allow_html=True,
                )
            with metric_cols[2]:
                st.markdown(
                    f'<div class="metric-card"><div class="metric-label">Actions</div><div class="metric-value">{len(analysis["action_items"])}</div></div>',
                    unsafe_allow_html=True,
                )

            st.markdown('<div class="section-title">📝 Summary</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-card">{analysis["summary"]}</div>', unsafe_allow_html=True)

            st.markdown('<div class="section-title">🎯 Key decisions</div>', unsafe_allow_html=True)
            decisions_html = "".join(f"<div class='info-card'>• {decision}</div>" for decision in analysis["decisions"])
            st.markdown(decisions_html, unsafe_allow_html=True)

            st.markdown('<div class="section-title">✅ Action items</div>', unsafe_allow_html=True)
            action_df = {
                "Task": [item[0] for item in analysis["action_items"]],
                "Owner": [item[1] for item in analysis["action_items"]],
                "Deadline": [item[2] for item in analysis["action_items"]],
            }
            st.table(action_df)

            st.markdown('<div class="section-title">🔑 Key topics</div>', unsafe_allow_html=True)
            topic_html = "".join(f"<span class='pill'>{topic}</span>" for topic in analysis["topics"])
            st.markdown(f'<div class="info-card">{topic_html}</div>', unsafe_allow_html=True)

            with st.expander("Transcript preview"):
                st.write(meeting_text)
        else:
            st.warning("Please provide a meeting transcript before analyzing.")

    st.markdown('</div>', unsafe_allow_html=True)

