from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
