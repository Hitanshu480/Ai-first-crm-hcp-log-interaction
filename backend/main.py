from fastapi import FastAPI
from pydantic import BaseModel
from agent.graph import build_graph

app = FastAPI()
agent = build_graph()

STATE = {}

class ChatRequest(BaseModel):
    message: str

def detect_intent(message: str):
    keywords = ["change", "update", "fix", "modify"]
    for k in keywords:
        if k in message.lower():
            return "edit"
    return "log"

@app.post("/agent/chat")
def chat(req: ChatRequest):
    global STATE

    intent = detect_intent(req.message)

    if intent == "edit":
        STATE = agent.invoke(
            input=req.message,
            state=STATE,
            config={"configurable": {"entrypoint": "edit"}}
        )
    else:
        STATE = agent.invoke(
            input=req.message,
            state=STATE,
            config={"configurable": {"entrypoint": "log"}}
        )

    return STATE
