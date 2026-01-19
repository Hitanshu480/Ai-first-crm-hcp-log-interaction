@app.post("/agent/chat")
def chat(req: ChatRequest):
    result = agent.invoke([HumanMessage(content=req.message)])
    return {"response": result[-1].content}
