# Ai-first-crm-hcp-log-interaction

AI-First CRM – HCP Log Interaction Module
 Overview

This project implements an AI-first CRM Log Interaction screen for Healthcare Professionals (HCPs).
Unlike traditional CRMs, the form is never filled manually. All interaction data is captured, corrected, and managed only through an AI Assistant using LangGraph and LLMs.

The system is designed from a life sciences field representative perspective, focusing on accuracy, compliance, and usability.

 Key Features

Log HCP interactions using natural language chat

Automatically extract:

HCP Name

Topics discussed

Sentiment

Materials shared

Follow-up actions

Correct mistakes via chat (example: “Change Dr Smith to Dr John and sentiment to negative”)

AI-controlled state management using LangGraph

Read-only form auto-populated from AI state

🏗️ Architecture
React UI (Read-only Form)
   ↓
AI Assistant Chat
   ↓
FastAPI Backend
   ↓
LangGraph Agent
   ↓
LLM (Groq – gemma2-9b-it)
   ↓
LangGraph Tools
   ↓
Central Interaction State

🧠 Why LangGraph?

LangGraph is used to:

Maintain persistent interaction state

Route user intent (log vs edit)

Ensure structured, deterministic workflows

Safely apply edits without overwriting existing data

🛠️ LangGraph Tools Implemented (5 Total)
1️⃣ Log Interaction Tool (Mandatory)

Converts free-text chat into structured interaction data

Uses LLM for summarization and entity extraction

2️⃣ Edit Interaction Tool (Mandatory)

Modifies only user-requested fields

Preserves all other existing data

3️⃣ Validate Interaction Tool

Ensures mandatory fields exist

Flags missing or inconsistent data

4️⃣ Suggest Follow-up Tool

Suggests next best actions based on sentiment and discussion

5️⃣ Compliance Check Tool

Flags potential promotional or non-compliant language

🔄 Interaction Flow Example

User Input (Chat):

“Today I met Dr Smith and discussed product X efficiency. Sentiment was positive and I shared brochures.”

➡️ AI extracts and populates form automatically.

User Correction (Chat):

“Change HCP name to Dr John and sentiment to negative. Keep everything else same.”

➡️ Only specified fields are updated via Edit Interaction Tool.

⚙️ Tech Stack

Frontend: React, Redux, Google Inter font

Backend: Python, FastAPI

AI Agent Framework: LangGraph

LLM: Groq – gemma2-9b-it

Database: PostgreSQL / MySQL (logical schema)

State Management: Redux + LangGraph
