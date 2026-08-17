import streamlit as st
from pathlib import Path
import speech_recognition as sr
from io import BytesIO

from backend.ai_service import analyze_meeting

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="MeetMind AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------- CUSTOM CSS ----------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fraunces:opsz,wght@9..144,500;9..144,600&display=swap');

    :root {
        --bg: #0b0e14;
        --panel: #12161f;
        --panel-soft: #161b26;
        --line: rgba(201, 178, 138, 0.16);
        --line-soft: rgba(255, 255, 255, 0.06);
        --text: #e9e7e1;
        --muted: #9a9a9a;
        --gold: #c9a962;
        --gold-soft: rgba(201, 169, 98, 0.12);
        --ink: #7d8ba1;
        --success: #6fae8f;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, sans-serif;
    }

    .stApp {
        background:
            radial-gradient(1200px 600px at 15% -10%, rgba(201, 169, 98, 0.05), transparent),
            linear-gradient(180deg, #08090d 0%, #0b0e14 45%, #0d1117 100%);
        color: var(--text);
    }

    #MainMenu, footer, header {visibility: hidden;}

    .main .block-container {
        padding-top: 2.5rem;
        padding-bottom: 4rem;
        max-width: 980px;
    }

    /* ---------- Hero ---------- */
    .hero {
        border-bottom: 1px solid var(--line);
        padding-bottom: 1.6rem;
        margin-bottom: 2.2rem;
    }

    .kicker {
        font-size: 11px;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        color: var(--gold);
        font-weight: 600;
        margin-bottom: 0.6rem;
    }

    .main-title {
        font-family: 'Fraunces', serif;
        font-size: 46px;
        font-weight: 600;
        letter-spacing: -0.02em;
        color: #f5f3ee;
        margin-bottom: 0.4rem;
        line-height: 1.1;
    }

    .tagline {
        color: var(--muted);
        font-size: 15.5px;
        max-width: 620px;
        line-height: 1.6;
        font-weight: 400;
    }

    /* ---------- Section headers ---------- */
    .section-title {
        font-family: 'Fraunces', serif;
        font-size: 21px;
        font-weight: 600;
        color: #f0eee8;
        margin: 2.4rem 0 0.9rem 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .section-title .num {
        font-family: 'Inter', sans-serif;
        font-size: 11px;
        color: var(--gold);
        letter-spacing: 0.1em;
        border: 1px solid var(--line);
        border-radius: 999px;
        padding: 3px 9px;
        font-weight: 600;
    }

    /* ---------- Panels / cards ---------- */
    .panel {
        background: var(--panel);
        border: 1px solid var(--line-soft);
        border-radius: 14px;
        padding: 1.4rem 1.5rem;
        margin-bottom: 1rem;
    }

    .info-card {
        background: var(--panel);
        border: 1px solid var(--line-soft);
        border-left: 2px solid var(--gold);
        border-radius: 10px;
        padding: 0.95rem 1.15rem;
        margin-bottom: 0.6rem;
        color: #ddd9cf;
        line-height: 1.65;
        font-size: 14.5px;
    }

    .summary-card {
        background: var(--panel);
        border: 1px solid var(--line-soft);
        border-radius: 14px;
        padding: 1.3rem 1.5rem;
        line-height: 1.75;
        font-size: 15px;
        color: #ddd9cf;
    }

    /* ---------- Metric cards ---------- */
    .metric-card {
        background: linear-gradient(160deg, var(--gold-soft), transparent 70%);
        border: 1px solid var(--line);
        border-radius: 14px;
        padding: 1.15rem 1.3rem;
        height: 100%;
    }

    .metric-label {
        font-size: 10.5px;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: var(--muted);
        font-weight: 600;
    }

    .metric-value {
        font-family: 'Fraunces', serif;
        font-size: 34px;
        font-weight: 600;
        margin-top: 0.35rem;
        color: #f5f3ee;
    }

    /* ---------- Topic pills ---------- */
    .pill {
        display: inline-block;
        padding: 0.4rem 0.85rem;
        border-radius: 999px;
        background: var(--gold-soft);
        border: 1px solid var(--line);
        color: #e6d9b8;
        margin: 0.2rem 0.4rem 0.2rem 0;
        font-size: 12.5px;
        font-weight: 500;
    }

    /* ---------- Inputs / buttons ---------- */
    .stTextArea textarea {
        background: var(--panel) !important;
        border: 1px solid var(--line-soft) !important;
        border-radius: 12px !important;
        color: var(--text) !important;
        font-size: 14.5px !important;
    }
    .stTextArea textarea:focus {
        border-color: var(--gold) !important;
        box-shadow: 0 0 0 1px var(--gold) !important;
    }

    .stButton > button {
        border-radius: 10px !important;
        border: 1px solid var(--line) !important;
        font-weight: 600 !important;
        letter-spacing: 0.01em;
    }

    .stButton > button[kind="primary"],
    div[data-testid="stButton"] button {
        background: linear-gradient(135deg, #c9a962, #b8934f) !important;
        color: #14110a !important;
        border: none !important;
    }

    div[data-testid="stFileUploader"] {
        background: var(--panel);
        border: 1px dashed var(--line);
        border-radius: 12px;
        padding: 0.4rem;
    }

    .stSelectbox > div > div {
        background: var(--panel) !important;
        border-radius: 10px !important;
        border: 1px solid var(--line-soft) !important;
    }

    /* ---------- Table ---------- */
    .stTable, .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid var(--line-soft);
    }

    hr {
        border-color: var(--line-soft) !important;
    }

    .toolbar-row {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        margin-bottom: 0.9rem;
        color: var(--muted);
        font-size: 13px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def load_sample_transcript(name: str) -> str:
    sample_path = Path(__file__).resolve().parent / "sample_data" / f"{name}.txt"
    return sample_path.read_text(encoding="utf-8") if sample_path.exists() else ""


# ---------------- HERO ----------------
st.markdown('<div class="hero">', unsafe_allow_html=True)
st.markdown('<div class="kicker">Meeting Intelligence</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">MeetMind AI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="tagline">Turn conversations into clear summaries, decisions, '
    'owners, deadlines, and practical next steps — in seconds.</div>',
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# ---------------- TRANSCRIPT INPUT ----------------
st.markdown('<div class="section-title"><span class="num">01</span> Meeting transcript</div>', unsafe_allow_html=True)

with st.container():
    top_col1, top_col2, top_col3 = st.columns([2, 1.2, 1])
    with top_col1:
        uploaded_file = st.file_uploader(
            "Upload a transcript (.txt)", type=["txt"], label_visibility="collapsed"
        )
    with top_col2:
        sample_options = ["team_meeting", "project_meeting", "hackathon_meeting"]
        selected_sample = st.selectbox("Sample transcript", sample_options, label_visibility="collapsed")
    with top_col3:
        if st.button("Load sample", use_container_width=True):
            st.session_state["manual_text"] = load_sample_transcript(selected_sample)

    rec_col, _ = st.columns([1, 3])
    with rec_col:
        if st.button("🎤  Record voice", use_container_width=True, help="Upload an audio recording to transcribe"):
            st.session_state["recording_active"] = True

    if st.session_state.get("recording_active", False):
        st.info("Upload an audio file below, or paste your transcript directly into the text area.")
        audio_file = st.file_uploader(
            "Upload audio file (.wav, .mp3, .ogg)", type=["wav", "mp3", "ogg"], key="audio_upload"
        )
        if audio_file is not None:
            try:
                st.info("Converting audio to text…")
                recognizer = sr.Recognizer()
                with sr.AudioFile(audio_file) as source:
                    audio = recognizer.record(source)
                    transcribed_text = recognizer.recognize_google(audio)
                    st.session_state["manual_text"] = transcribed_text
                    st.success("Audio converted to text successfully.")
                    st.session_state["recording_active"] = False
            except sr.UnknownValueError:
                st.error("Could not understand the audio. Please try again with clearer audio.")
            except sr.RequestError:
                st.error("Error connecting to the speech recognition service. Please try again.")

    if uploaded_file is not None:
        meeting_text = uploaded_file.read().decode("utf-8")
    else:
        meeting_text = st.session_state.get("manual_text", "")

    meeting_text = st.text_area(
        "Paste a meeting transcript",
        value=meeting_text,
        height=240,
        placeholder="Example: We reviewed product progress, assigned follow-ups, and confirmed the final delivery deadline...",
        label_visibility="collapsed",
    )

    analyze = st.button("✨  Analyze meeting", use_container_width=False, type="primary")

# ---------------- ANALYSIS ----------------
if analyze:
    if meeting_text.strip():
        analysis = analyze_meeting(meeting_text)

        st.markdown('<div class="section-title"><span class="num">02</span> Meeting overview</div>', unsafe_allow_html=True)
        metric_cols = st.columns(3)
        with metric_cols[0]:
            st.markdown(
                f'<div class="metric-card"><div class="metric-label">Words</div>'
                f'<div class="metric-value">{analysis["word_count"]}</div></div>',
                unsafe_allow_html=True,
            )
        with metric_cols[1]:
            st.markdown(
                f'<div class="metric-card"><div class="metric-label">Decisions</div>'
                f'<div class="metric-value">{len(analysis["decisions"])}</div></div>',
                unsafe_allow_html=True,
            )
        with metric_cols[2]:
            st.markdown(
                f'<div class="metric-card"><div class="metric-label">Actions</div>'
                f'<div class="metric-value">{len(analysis["action_items"])}</div></div>',
                unsafe_allow_html=True,
            )

        st.markdown('<div class="section-title"><span class="num">03</span> Summary</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="summary-card">{analysis["summary"]}</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-title"><span class="num">04</span> Key decisions</div>', unsafe_allow_html=True)
        if analysis["decisions"]:
            decisions_html = "".join(
                f"<div class='info-card'>{decision}</div>" for decision in analysis["decisions"]
            )
            st.markdown(decisions_html, unsafe_allow_html=True)
        else:
            st.markdown('<div class="info-card">No decisions were detected in this transcript.</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-title"><span class="num">05</span> Action items</div>', unsafe_allow_html=True)
        if analysis["action_items"]:
            action_df = {
                "Task": [item[0] for item in analysis["action_items"]],
                "Owner": [item[1] for item in analysis["action_items"]],
                "Deadline": [item[2] for item in analysis["action_items"]],
            }
            st.table(action_df)
        else:
            st.markdown('<div class="info-card">No action items were detected in this transcript.</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-title"><span class="num">06</span> Key topics</div>', unsafe_allow_html=True)
        topic_html = "".join(f"<span class='pill'>{topic}</span>" for topic in analysis["topics"])
        st.markdown(f'<div class="panel">{topic_html}</div>', unsafe_allow_html=True)

        with st.expander("Transcript preview"):
            st.write(meeting_text)
    else:
        st.warning("Please provide a meeting transcript before analyzing.")