from fastapi import FastAPI
from schemas import ChatRequest
from prompts import get_system_prompt
from llm import get_response

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API running"}

@app.post("/chat")
def chat(req: ChatRequest):
    try:
        system_prompt = {
            "role": "system",
            "content": get_system_prompt(req.role)
        }

        messages = [system_prompt] + [
            {"role": m.role, "content": m.content} for m in req.messages
        ]

        reply = get_response(messages)

        return {"response": reply}

    except Exception as e:
        print("ERROR:", str(e))
        return {"response": "Server error occurred"}