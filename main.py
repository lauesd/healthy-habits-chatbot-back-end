from fastapi import FastAPI
from pydantic import BaseModel
from services.chat_service import process_message

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def hello_world():
    return {"message": "Hello World"}

@app.post("/chat")
def chat(request: ChatRequest):
    return process_message(request.message)