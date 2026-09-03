from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Ataa-Backend"
    APP_ENV: str = "development"
    DEBUG: bool = True
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "https://yzes95.github.io",
    ]

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/ataa_db"

    # AWS Configuration
    AWS_REGION: str = "eu-central-1"
    AWS_S3_BUCKET: str = "ataa-verification-documents"

    # TODO: Add JWT secret, payment keys, and external API credentials as needed

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
