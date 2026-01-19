from fastapi import FastAPI
from pydantic import BaseModel
from agent.graph import build_graph
from langchain_core.messages import HumanMessage

app = FastAPI()
agent = build_graph()

class ChatRequest(BaseModel):
    message: str

@app.post("/agent/chat")
def chat(req: ChatRequest):
    result = agent.invoke([HumanMessage(content=req.message)])
    return {"response": result[-1].content}
