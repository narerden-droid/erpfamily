from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_env: str = "development"
    database_url: str = "postgresql+psycopg://family_erp:family_erp@localhost:5432/family_erp"
    secret_key: str = "dev-only-change-me"
    default_currency: str = "KZT"
    default_timezone: str = "Asia/Almaty"
    session_cookie_secure: bool = True

    @property
    def is_production(self) -> bool:
        return self.app_env == "production"


@lru_cache
def get_settings() -> Settings:
    s = Settings()
    if s.is_production and s.secret_key == "dev-only-change-me":
        raise RuntimeError("SECRET_KEY must be set in production")
    return s
