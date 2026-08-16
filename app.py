import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="MeetMind AI",
    page_icon="🧠",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    :root {
        --bg: #f6f7ff;
        --panel: rgba(255, 255, 255, 0.8);
        --panel-strong: #ffffff;
        --border: rgba(148, 163, 184, 0.24);
        --text: #111827;
        --muted: #5f6b7d;
        --primary: #5b5ce6;
        --purple: #8b5cf6;
        --pink: #ec4899;
        --blue: #3b82f6;
        --shadow: 0 18px 50px rgba(15, 23, 42, 0.08);
    }

    .stApp {
        background: radial-gradient(circle at top left, rgba(139, 92, 246, 0.10), transparent 26%),
                    radial-gradient(circle at top right, rgba(59, 130, 246, 0.10), transparent 24%),
                    linear-gradient(180deg, #f8f8ff 0%, #f3f6fb 100%);
    }

    .main-title {
        font-size: clamp(2.3rem, 4vw, 3.5rem);
        font-weight: 800;
        letter-spacing: -0.06em;
        margin: 0;
        color: var(--text);
    }

    .hero-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.96), rgba(246,247,255,0.9));
        border: 1px solid var(--border);
        border-radius: 26px;
        box-shadow: var(--shadow);
        padding: 1.6rem 1.7rem;
        margin-bottom: 1.5rem;
        position: relative;
        overflow: hidden;
    }

    .hero-card::before {
        content: "";
        position: absolute;
        width: 260px;
        height: 260px;
        right: -60px;
        bottom: -85px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(91, 92, 230, 0.14), transparent 68%);
        pointer-events: none;
    }

    .brand-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
        flex-wrap: wrap;
    }

    .brand-group {
        display: flex;
        align-items: center;
        gap: 0.85rem;
    }

    .brand-icon {
        width: 46px;
        height: 46px;
        border-radius: 14px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, var(--primary), var(--purple));
        color: white;
        font-size: 1.3rem;
        box-shadow: 0 14px 26px rgba(91, 92, 230, 0.25);
    }

    .subtitle {
        font-size: 1.05rem;
        color: var(--muted);
        margin-top: 0.8rem;
        max-width: 760px;
        line-height: 1.5;
    }

    .ai-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.52rem 0.9rem;
        border-radius: 999px;
        background: rgba(91, 92, 230, 0.08);
        color: var(--primary);
        border: 1px solid rgba(91, 92, 230, 0.18);
        font-weight: 700;
        font-size: 0.8rem;
        letter-spacing: 0.01em;
    }

    .status-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #20c997;
        box-shadow: 0 0 0 4px rgba(32, 201, 151, 0.12);
    }

    .section-title {
        font-size: 1.3rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        color: var(--text);
        margin: 0;
    }

    .section-subtitle {
        color: var(--muted);
        font-size: 0.95rem;
        margin: 0.35rem 0 0.85rem;
    }

    .upload-box {
        border: 1.5px dashed rgba(91, 92, 230, 0.28);
        border-radius: 18px;
        background: linear-gradient(180deg, rgba(91,92,230,0.04), rgba(59,130,246,0.02));
        padding: 1rem;
        margin-bottom: 0.9rem;
        transition: all 0.2s ease;
    }

    .upload-box:hover {
        border-color: rgba(91, 92, 230, 0.45);
        transform: translateY(-1px);
    }

    .upload-label {
        font-size: 0.95rem;
        font-weight: 700;
        color: var(--text);
    }

    .upload-meta {
        color: var(--muted);
        font-size: 0.8rem;
        margin-top: 0.2rem;
    }

    div[data-testid="stFileUploader"] section {
        border-radius: 18px !important;
        border: 1px solid rgba(148, 163, 184, 0.48) !important;
        background: rgba(255,255,255,0.9) !important;
    }

    div[data-testid="stTextArea"] textarea {
        min-height: 220px !important;
        border-radius: 18px !important;
        border: 1px solid rgba(148, 163, 184, 0.48) !important;
        padding: 1rem 1rem !important;
        background: rgba(255,255,255,0.9) !important;
        transition: all 0.2s ease;
    }

    div[data-testid="stTextArea"] textarea:focus {
        border-color: rgba(91, 92, 230, 0.75) !important;
        box-shadow: 0 0 0 4px rgba(91, 92, 230, 0.10) !important;
    }

    .cta-button {
        width: 100%;
        border-radius: 16px !important;
        background: linear-gradient(135deg, var(--primary), var(--purple)) !important;
        color: white !important;
        border: none !important;
        padding: 0.9rem 1.2rem !important;
        font-size: 1rem !important;
        font-weight: 700 !important;
        box-shadow: 0 18px 26px rgba(91, 92, 230, 0.22) !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease !important;
    }

    .cta-button:hover {
        transform: translateY(-1px);
        box-shadow: 0 20px 30px rgba(91, 92, 230, 0.28) !important;
    }

    .cta-button:disabled {
        opacity: 0.75 !important;
        cursor: wait !important;
    }

    .feature-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 1rem;
        margin-top: 1.4rem;
    }

    .feature-card {
        background: rgba(255,255,255,0.8);
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 1.1rem 1rem;
        box-shadow: 0 12px 24px rgba(15, 23, 42, 0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .feature-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 18px 30px rgba(15, 23, 42, 0.06);
    }

    .feature-icon {
        width: 42px;
        height: 42px;
        border-radius: 12px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, rgba(91,92,230,0.12), rgba(59,130,246,0.08));
        color: var(--primary);
        font-size: 1.15rem;
        margin-bottom: 0.7rem;
    }

    .feature-title {
        font-size: 1rem;
        font-weight: 800;
        margin: 0;
        color: var(--text);
    }

    .feature-text {
        color: var(--muted);
        font-size: 0.88rem;
        margin: 0.4rem 0 0;
        line-height: 1.5;
    }

    .empty-state {
        background: linear-gradient(180deg, rgba(255,255,255,0.9), rgba(249,250,255,0.9));
        border: 1px solid var(--border);
        border-radius: 22px;
        padding: 2rem 1.1rem;
        text-align: center;
        margin-top: 1.2rem;
    }

    .empty-icon {
        width: 68px;
        height: 68px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border-radius: 20px;
        background: linear-gradient(135deg, rgba(91,92,230,0.12), rgba(59,130,246,0.08));
        font-size: 2rem;
        margin-bottom: 0.7rem;
    }

    .empty-title {
        margin: 0;
        font-size: 1.2rem;
        font-weight: 800;
        color: var(--text);
    }

    .empty-body {
        margin: 0.55rem auto 0;
        max-width: 520px;
        color: var(--muted);
        line-height: 1.6;
    }

    .result-card {
        background: rgba(255,255,255,0.9);
        border: 1px solid var(--border);
        border-radius: 20px;
        box-shadow: 0 12px 24px rgba(15, 23, 42, 0.04);
        padding: 1.1rem 1.1rem 1rem;
        margin-top: 1.2rem;
    }

    .result-card h3 {
        margin: 0 0 0.7rem;
        font-size: 1.08rem;
        font-weight: 800;
        color: var(--text);
        letter-spacing: -0.02em;
    }

    .result-copy {
        margin: 0;
        color: var(--text);
        line-height: 1.7;
    }

    .decision-list {
        list-style: none;
        padding: 0;
        margin: 0;
        display: grid;
        gap: 0.6rem;
    }

    .decision-list li {
        background: rgba(91,92,230,0.04);
        border: 1px solid rgba(91,92,230,0.10);
        border-radius: 12px;
        padding: 0.75rem 0.8rem;
        color: var(--text);
        line-height: 1.5;
    }

    .topic-badges {
        display: flex;
        flex-wrap: wrap;
        gap: 0.55rem;
    }

    .topic-badge {
        display: inline-flex;
        align-items: center;
        padding: 0.5rem 0.75rem;
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.78rem;
        background: linear-gradient(135deg, rgba(91,92,230,0.10), rgba(59,130,246,0.08));
        border: 1px solid rgba(91,92,230,0.12);
        color: var(--primary);
    }

    .action-row {
        display: grid;
        grid-template-columns: 2.2fr 1fr 1fr 1fr;
        gap: 0.8rem;
        align-items: center;
        background: rgba(248,250,252,0.9);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 0.8rem 0.9rem;
        margin-top: 0.7rem;
    }

    .action-header {
        font-size: 0.76rem;
        font-weight: 800;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        color: var(--muted);
    }

    .action-cell {
        color: var(--text);
        font-size: 0.92rem;
    }

    .status-pill {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-width: 86px;
        padding: 0.32rem 0.6rem;
        border-radius: 999px;
        font-size: 0.72rem;
        font-weight: 700;
    }

    .pending { background: rgba(245,158,11,0.12); color: #b45309; }
    .progress { background: rgba(59,130,246,0.12); color: #1d4ed8; }
    .complete { background: rgba(22,163,74,0.12); color: #15803d; }

    @media (max-width: 900px) {
        .feature-grid { grid-template-columns: 1fr; }
        .action-row { grid-template-columns: 1fr 1fr; }
    }

    @media (max-width: 640px) {
        .hero-card {
            padding: 1.2rem 1rem;
            border-radius: 20px;
        }
        .brand-row {
            align-items: flex-start;
        }
        .action-row {
            grid-template-columns: 1fr;
        }
    }
</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------
st.markdown(
    """
    <div class="hero-card">
        <div class="brand-row">
            <div class="brand-group">
                <div class="brand-icon">🧠</div>
                <div class="main-title">MeetMind AI</div>
            </div>
            <div class="ai-pill"><span class="status-dot"></span>AI-Powered Meeting Intelligence</div>
        </div>
        <div class="subtitle">
            Transform meeting conversations into summaries, decisions, and actionable tasks.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# ---------------- INPUT SECTION ----------------
st.markdown(
    """
    <div class="section-title">Meeting Transcript</div>
    <div class="section-subtitle">Upload a transcript or paste your meeting conversation below.</div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="upload-box">
        <div class="upload-label">📄 Upload transcript</div>
        <div class="upload-meta">TXT files supported • Paste or drag in your meeting notes</div>
    </div>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    label="",
    type=["txt"],
    label_visibility="collapsed"
)

if uploaded_file is not None:
    meeting_text = uploaded_file.read().decode("utf-8")
else:
    meeting_text = st.text_area(
        label="",
        height=220,
        placeholder="Example: Today we discussed project progress, responsibilities, and the final submission timeline...",
        label_visibility="collapsed"
    )

st.caption("Tip: paste a transcript or upload a text file to get a quick summary and action list.")

analyze = st.button(
    "✨ Analyze Meeting",
    use_container_width=True,
    key="analyze_meeting_button"
)

# ---------------- QUICK FEATURE CARDS ----------------
feature_cards = [
    ("📝", "Smart Summary", "Get concise meeting summaries."),
    ("🎯", "Key Decisions", "Automatically identify important decisions."),
    ("✅", "Action Items", "Extract tasks, owners and deadlines."),
]

features_html = "".join(
    f"""
    <div class="feature-card">
        <div class="feature-icon">{icon}</div>
        <h4 class="feature-title">{title}</h4>
        <p class="feature-text">{text}</p>
    </div>
    """
    for icon, title, text in feature_cards
)

st.markdown(f'<div class="feature-grid">{features_html}</div>', unsafe_allow_html=True)


# ---------------- RESULTS ----------------
if analyze:
    if meeting_text.strip():
        st.success("Meeting transcript received successfully!")

        st.markdown(
            """
            <div class="result-card">
                <h3>Executive Summary</h3>
                <p class="result-copy">The team discussed the project progress, upcoming tasks, responsibilities, and submission deadlines. The conversation highlighted the need to complete the database work first, prepare the presentation after development, and finish final testing before submission.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="result-card">
                <h3>Key Decisions</h3>
                <ul class="decision-list">
                    <li>Database development will be completed first.</li>
                    <li>Presentation preparation will start after development.</li>
                    <li>Final testing will be completed before submission.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="result-card">
                <h3>Action Items</h3>
                <div class="action-row">
                    <div class="action-header">Task</div>
                    <div class="action-header">Owner</div>
                    <div class="action-header">Deadline</div>
                    <div class="action-header">Status</div>
                </div>
                <div class="action-row">
                    <div class="action-cell">Prepare database</div>
                    <div class="action-cell">Rahul</div>
                    <div class="action-cell">Friday</div>
                    <div><span class="status-pill pending">Pending</span></div>
                </div>
                <div class="action-row">
                    <div class="action-cell">Design presentation</div>
                    <div class="action-cell">Priya</div>
                    <div class="action-cell">Monday</div>
                    <div><span class="status-pill progress">In Progress</span></div>
                </div>
                <div class="action-row">
                    <div class="action-cell">Test application</div>
                    <div class="action-cell">Amit</div>
                    <div class="action-cell">Before submission</div>
                    <div><span class="status-pill complete">Completed</span></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="result-card">
                <h3>Important Topics</h3>
                <div class="topic-badges">
                    <span class="topic-badge">Database</span>
                    <span class="topic-badge">Presentation</span>
                    <span class="topic-badge">Testing</span>
                    <span class="topic-badge">Submission</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Please enter a meeting transcript first.")

else:
    st.markdown(
        """
        <div class="empty-state">
            <div class="empty-icon">✨</div>
            <h4 class="empty-title">Your meeting insights will appear here</h4>
            <p class="empty-body">Once you paste or upload a transcript, MeetMind AI will generate an executive summary, key decisions, and action items.</p>
        </div>
        """,
        unsafe_allow_html=True
    )