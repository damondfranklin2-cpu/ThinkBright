from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI Starter")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

settings = Settings()
