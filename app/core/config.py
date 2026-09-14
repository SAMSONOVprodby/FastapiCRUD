import os

from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

database_url=os.getenv("DATABASE_URL")
cors_origins= os.getenv("CORS_ORIGINS")

@dataclass(frozen=True)
class Settings:
    database_url: str
    cors_origins: str


def get_settings() -> Settings:
    return Settings(
        database_url=database_url,
        cors_origins=cors_origins
    )