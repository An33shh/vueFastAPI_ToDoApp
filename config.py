from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI"

    class Config:
        env_file = ".env"