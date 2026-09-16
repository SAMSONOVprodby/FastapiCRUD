import os
from dataclasses import dataclass, field
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()


def _require_env(name: str) -> str:
    value = os.getenv(name)
    if value is None:
        raise RuntimeError(f"Environment variable {name} is not set")
    return value


@dataclass(frozen=True)
class Settings:
    database_url: str
    cors_origins: list[str] = field(default_factory=list)


@lru_cache
def get_settings() -> Settings:
    raw_origins = os.getenv("CORS_ORIGINS", "")
    return Settings(
        database_url=_require_env("DATABASE_URL"),
        cors_origins=[o.strip() for o in raw_origins.split(",") if o.strip()],
    )
