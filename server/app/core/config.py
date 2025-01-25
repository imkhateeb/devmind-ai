from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    KAFKA_BROKER_URL: str
    RATE_LIMIT: int

    class Config:
        env_file = ".env"

settings = Settings()
