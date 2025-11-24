# app/core/config.py
from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "IEP Assistant"
    DATABASE_URL: str = "sqlite:///./iep.db"  # for dev only, not prod PHI
    # Later: SECRET_KEY, AUTH_CONFIG, CORS origins, etc.

    class Config:
        env_file = ".env"


settings = Settings()
