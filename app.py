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

.main-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 0px;
}

.subtitle {
    font-size: 18px;
    margin-top: 0px;
}

.section-title {
    font-size: 24px;
    font-weight: 600;
    margin-top: 25px;
}

.info-card {
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #dddddd;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------
st.markdown(
    '<div class="main-title">🧠 MeetMind AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Meeting Intelligence & Action Item Generator</div>',
    unsafe_allow_html=True
)

st.write(
    "Transform meeting discussions into clear summaries, "
    "decisions, and actionable tasks."
)

st.divider()


# ---------------- INPUT SECTION ----------------
st.markdown(
    '<div class="section-title">📋 Meeting Transcript</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "📂 Or upload a meeting transcript",
    type=["txt"]
)

if uploaded_file is not None:
    meeting_text = uploaded_file.read().decode("utf-8")
else:
    meeting_text = st.text_area(
        "Paste your meeting transcript below:",
        height=250,
        placeholder="Example: Today we discussed the college project..."
    )


analyze = st.button(
    "✨ Analyze Meeting",
    use_container_width=True
)


# ---------------- RESULTS ----------------
if analyze:

    if meeting_text.strip():

        st.success("Meeting transcript received successfully!")

        # ---------- SUMMARY ----------
        st.markdown(
            '<div class="section-title">📝 Meeting Summary</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="info-card">'
            'The team discussed the project progress, upcoming tasks, '
            'responsibilities, and submission deadlines.'
            '</div>',
            unsafe_allow_html=True
        )

        # ---------- DECISIONS ----------
        st.markdown(
            '<div class="section-title">🎯 Key Decisions</div>',
            unsafe_allow_html=True
        )

        st.markdown("""
        <div class="info-card">

        • Database development will be completed first.<br>
        • Presentation preparation will start after development.<br>
        • Final testing will be completed before submission.

        </div>
        """, unsafe_allow_html=True)


        # ---------- ACTION ITEMS ----------
        st.markdown(
            '<div class="section-title">✅ Action Items</div>',
            unsafe_allow_html=True
        )

        action_data = {
            "Task": [
                "Prepare database",
                "Design presentation",
                "Test application"
            ],
            "Responsible": [
                "Rahul",
                "Priya",
                "Amit"
            ],
            "Deadline": [
                "Friday",
                "Monday",
                "Before submission"
            ]
        }

        st.table(action_data)


        # ---------- KEY TOPICS ----------
        st.markdown(
            '<div class="section-title">🔑 Key Topics</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            "Database &nbsp;&nbsp; | &nbsp;&nbsp; "
            "Presentation &nbsp;&nbsp; | &nbsp;&nbsp; "
            "Testing &nbsp;&nbsp; | &nbsp;&nbsp; "
            "Submission",
            unsafe_allow_html=True
        )

    else:

        st.warning("Please enter a meeting transcript first.")