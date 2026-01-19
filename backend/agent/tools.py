import json
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="gemma2-9b-it",
    api_key="YOUR_GROQ_API_KEY"
)

# TOOL 1: Log Interaction
def log_interaction_tool(message: str, state: dict):
    prompt = f"""
Extract details from this interaction.
Return JSON with keys:
hcp_name, topics_discussed, sentiment, materials_shared

Text:
{message}
"""
    result = llm.invoke(prompt).content
    extracted = json.loads(result)
    state.update(extracted)
    return state


# TOOL 2: Edit Interaction
def edit_interaction_tool(message: str, state: dict):
    prompt = f"""
Current data:
{state}

User wants to change some fields:
{message}

Return ONLY updated JSON.
"""
    updated = json.loads(llm.invoke(prompt).content)
    state.update(updated)
    return state


# TOOL 3: Validate Interaction
def validate_interaction_tool(state: dict):
    if not state.get("hcp_name"):
        state["hcp_name"] = "UNKNOWN"
    if not state.get("sentiment"):
        state["sentiment"] = "UNKNOWN"
    return state


# TOOL 4: Suggest Follow-up
def followup_tool(state: dict):
    prompt = f"""
Suggest next action based on sentiment:
{state.get('sentiment')}
"""
    state["follow_up_actions"] = llm.invoke(prompt).content
    return state


# TOOL 5: Compliance Check
def compliance_tool(state: dict):
    prompt = f"""
Check compliance for this topic:
{state.get('topics_discussed')}
Return SAFE or FLAGGED.
"""
    state["compliance_status"] = llm.invoke(prompt).content
    return state

