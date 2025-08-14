from fastapi import APIRouter
from app.models.hello_model import HelloResponse

router = APIRouter()

@router.get("/hello", response_model=HelloResponse)
def say_hello():
    return {"message": "Hello, world!"}
