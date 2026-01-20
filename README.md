# AI-First CRM – HCP Log Interaction Module

## Overview
This project demonstrates an AI-first Customer Relationship Management (CRM) module
for Life Sciences, focused on logging Healthcare Professional (HCP) interactions.

The system allows field representatives to log interactions using:
1. A structured form
2. A conversational AI chat interface

The AI agent is built using LangGraph and Groq LLM.

---

## Tech Stack
- Frontend: React, Redux-style state handling
- Backend: Python, FastAPI
- AI Agent Framework: LangGraph
- LLM: Groq (gemma2-9b-it)
- Database: Conceptual (PostgreSQL/MySQL ready)
- Font: Google Inter

---

## Key Features
- Dual input: Form + Conversational Chat
- AI-driven extraction of:
  - Doctor name
  - Sentiment
  - Interaction summary
- Automatic follow-up suggestions
- Product feedback identification

---

## LangGraph AI Agent Tools

1. **Log Interaction Tool**
   - Extracts HCP name, sentiment, and summary using LLM

2. **Edit Interaction Tool**
   - Modifies previously logged interactions based on user instruction

3. **Capture Product Feedback Tool**
   - Detects issues like delivery delays or product complaints

4. **Schedule Follow-up Tool**
   - Automatically schedules follow-ups for negative interactions

5. **Generate Final Summary Tool**
   - Produces a structured final interaction summary

---

## Architecture Flow
1. User enters interaction via chat or form
2. Request sent to FastAPI backend
3. LangGraph agent processes request using tools
4. Structured interaction state is returned
5. Frontend UI updates automatically

---

## How to Run

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
