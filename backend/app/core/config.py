from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    app_env: str = Field(default="development")

    database_url: str = Field(
        default="postgresql+psycopg://gov_signal:gov_signal_dev@localhost:5433/gov_signal"
    )

    anthropic_api_key: str = Field(default="")
    anthropic_model: str = Field(default="claude-sonnet-4-6")

    log_level: str = Field(default="INFO")


settings = Settings()
