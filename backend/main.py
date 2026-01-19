if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.messages import HumanMessage

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/agent/chat")
def chat(req: ChatRequest):
    # IMPORT LANGGRAPH ONLY AT RUNTIME
    from agent.graph import build_graph

    agent = build_graph()  # lazy compile (runtime)
    result = agent.invoke(req.message)

    return {"response": result}
