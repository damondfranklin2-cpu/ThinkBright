from fastapi import FastAPI
from app.routes import hello, ai
from app.config import settings

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

app.include_router(hello.router)
app.include_router(ai.router)
