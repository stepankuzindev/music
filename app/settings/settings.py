from pydantic import BaseSettings


class Settings(BaseSettings):
    API_NAME: str = "Music API"
    POSTGRES_URL: str = "postgresql://postgres:postgres@postgres:5432"
    SENTRY_DSN: str = ""


settings = Settings()
