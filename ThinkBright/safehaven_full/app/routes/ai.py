from fastapi import APIRouter
from pydantic import BaseModel
from app.config import settings
import openai

openai.api_key = settings.OPENAI_API_KEY

router = APIRouter()

class AIRequest(BaseModel):
    prompt: str

class AIResponse(BaseModel):
    reply: str

@router.post("/ai", response_model=AIResponse)
def ai_chat(data: AIRequest):
    completion = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are SafeHaven AI, a supportive mental health companion."},
            {"role": "user", "content": data.prompt}
        ]
    )
    return {"reply": completion.choices[0].message.content}
