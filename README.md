# 🧠 MeetMind AI

# 🧠 MeetMind AI

### AI-Powered Meeting Intelligence & Action Item Generator

MeetMind AI is a smart meeting assistant that transforms raw discussion notes into structured, decision-ready outputs.

It helps teams turn long conversations into clear summaries, key decisions, action items, owners, deadlines, and important topics without manually reviewing every transcript.

---

## 🚀 Problem

Meetings generate a lot of value, but most of it is lost in long, unstructured discussion threads. Important decisions, responsibilities, and follow-ups are easy to miss.

Without a structured summary, teams waste time re-reading transcripts and chasing unclear next steps.

MeetMind AI addresses this by automatically analyzing meeting content and converting it into useful, decision-oriented insight.

---

## 💡 Solution

MeetMind AI accepts meeting transcripts as input and applies AI-driven text analysis to extract meaningful information.

### Input sources

- 📝 Manual transcript entry
- 📂 TXT file upload
- 📊 Sample meeting transcripts for testing

### Processing capabilities

- Generative AI summarization
- Text analysis and key phrase extraction
- Decision identification
- Action item extraction
- Person and deadline detection
- Topic clustering and keyword recognition
- Content safety screening

### Output generated

- 📝 Meeting summary
- 🎯 Key decisions
- ✅ Action items
- 👤 Responsible owners
- 📅 Deadlines and due dates
- 🔑 Key topics and keywords

---

## ✨ Core features

### 📝 AI meeting summarization
Converts long discussion text into concise, readable summaries.

### 🎯 Key decision extraction
Identifies the most important decisions made in a meeting.

### ✅ Action item generation
Extracts tasks that require follow-up after the meeting.

### 👤 Responsibility mapping
Highlights the people assigned to specific tasks or deliverables.

### 📅 Deadline detection
Detects dates, milestones, and time-sensitive follow-ups.

### 🔑 Topic extraction
Surfaces the most relevant themes and discussion points.

### 🛡️ Content safety
Uses filtering to help prevent harmful or inappropriate content from being processed.

### 📊 Structured dashboard output
Presents results in a clean, easy-to-understand interface.

---

## 🏗️ System architecture

```text
                     ┌──────────────────────┐
                     │        User          │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │   MeetMind AI App    │
                     │      Streamlit       │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │ Meeting Transcript    │
                     │ Text / TXT Upload     │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │ Content Filtering     │
                     └──────────┬───────────┘
                                │
                                ▼
              ┌──────────────────────────────────────┐
              │         AI + Text Analysis            │
              │                                      │
              │ • Summarization                       │
              │ • Decision extraction                 │
              │ • Action item detection               │
              │ • Deadlines and ownership             │
              │ • Topic classification                │
              └──────────────┬───────────────────────┘
                             │
                             ▼
              ┌──────────────────────────────────────┐
              │      Structured Meeting Insights      │
              │                                      │
              │ • Summary                             │
              │ • Key decisions                       │
              │ • Action items                        │
              │ • Responsible people                  │
              │ • Deadlines                           │
              │ • Key topics                          │
              └──────────────────────────────────────┘
```

---

## 🧪 Project setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   streamlit run app.py
   ```

3. Upload or paste a transcript, then click Analyze meeting.

---

## 📌 Intended use

MeetMind AI is designed for:

- Team meetings
- Project reviews
- Hackathon planning sessions
- Client status updates
- Internal sprint discussions

It helps teams quickly capture what matters and convert discussion into action.