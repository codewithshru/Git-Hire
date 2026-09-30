"""Application settings loaded from environment variables (.env).

Secrets are never hardcoded — see backend/.env.example for required variables.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Application
    app_name: str = "GitHire API"
    environment: str = "development"
    debug: bool = True

    # CORS (Vite dev server origins)
    cors_origins: list[str] = ["http://localhost:5173", "http://localhost:3000"]

    # Database (local PostgreSQL 16)
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/githire"
    database_echo: bool = False

    # Redis (local Memurai)
    redis_url: str = "redis://localhost:6379/0"

    # Auth
    jwt_secret_key: str = "change-me-in-production"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 14

    # OAuth (provide via .env)
    google_client_id: str = ""
    google_client_secret: str = ""
    github_client_id: str = ""
    github_client_secret: str = ""

    # AI provider (adapter-based; vendor selected via env)
    ai_provider: str = "openai"
    openai_api_key: str = ""
    anthropic_api_key: str = ""

    # Storage
    aws_region: str = "ap-south-1"
    aws_access_key_id: str = ""
    aws_secret_access_key: str = ""
    s3_bucket_name: str = "githire-local"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
