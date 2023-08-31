from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    # Database configuration
    db_host: str
    db_port: str
    db_user: str
    db_password: str
    db_name: str

    model_config = SettingsConfigDict(
        env_prefix="APP_", env_file=".env", env_file_encoding="utf-8"
    )


@lru_cache
def get_db_settings() -> DBSettings:
    return DBSettings()
