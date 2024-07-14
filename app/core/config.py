from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_USER: Optional[str] = None
    POSTGRES_PASSWORD: Optional[str] = None
    POSTGRES_DB: Optional[str] = None
    POSTGRES_HOST: Optional[str] = None
    POSTGRES_PORT: Optional[str] = None
    SSL_KEY_PATH: Optional[str] = None
    SSL_CERT_PATH: Optional[str] = None
    SSL_KEY_SERVER: Optional[str] = None
    SSL_CERT_SERVER: Optional[str] = None
    DATABASE_URL: Optional[str] = None

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
