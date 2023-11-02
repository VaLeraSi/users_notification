from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class SmtpSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="SMTP_"
    )
    smtp_host: str = Field(alias="SMTP_HOST")
    smtp_port: int = Field(alias="SMTP_PORT")
    smtp_login: str = Field(alias="SMTP_LOGIN")
    smtp_password: str = Field(alias="SMTP_PASSWORD")
    smtp_email: str = Field(alias="SMTP_EMAIL")
    smtp_name: str = Field(alias="SMTP_NAME")


class EmailSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="TO_"
    )
    email: str = Field(alias="TO_EMAIL")


class SiteSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="SITE_"
    )
    port: int = Field(alias="SITE_PORT")
    host: str = Field("0.0.0.0", alias="SITE_HOST")


class MongoSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="DB_"
    )
    mongo_uri: str = Field(alias="DB_URI")


mongo_settings = MongoSettings()

db_name = "mongo_db"
client = AsyncIOMotorClient(mongo_settings.mongo_uri)
db = client[db_name]


class Settings(BaseSettings):
    SMTP: SmtpSettings
    SITE: SiteSettings
    EMAIL: EmailSettings


settings = Settings(
    SMTP=SmtpSettings(),
    EMAIL=EmailSettings(),
    SITE=SiteSettings(),
)
