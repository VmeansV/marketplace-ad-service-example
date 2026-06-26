from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5434/ads_db"
    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"
    kafka_bootstrap_servers: str = Field(
        default="localhost:9092",
        validation_alias=AliasChoices("KAFKA_BOOTSTRAP_SERVERS", "KAFKA_BROKERS"),
    )
    kafka_topic_ads: str = Field(
        default="ads",
        validation_alias=AliasChoices("KAFKA_TOPIC_ADS", "KAFKA_TOPIC_MARKETPLACE_ADS"),
    )

    auth_service_url: str = "http://localhost:8000"
