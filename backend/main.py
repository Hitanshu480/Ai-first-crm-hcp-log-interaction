from fastapi import FastAPI
from pydantic import BaseModel
from agent.graph import build_graph

app = FastAPI()
agent = build_graph()
STATE = {}

class ChatRequest(BaseModel):
    message: str

@app.post("/agent/chat")
def chat(req: ChatRequest):
    global STATE
    STATE = agent.invoke(req.message, STATE)
    return STATE

