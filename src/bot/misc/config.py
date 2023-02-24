from typing import Optional

from pydantic import BaseSettings, Field


class Config(BaseSettings):
    TOKEN: Optional[str] = Field(env="TOKEN")
    POSTGRES_URL: str = Field(
        env="POSTGRES_URL",
        default="postgresql://postgres:mypassword@localhost:5432/mydb",
    )

    CMD_PREFIX: str = "."

    class Config:
        case_sensitive = False
        env_prefix = ""
        env_file_encoding = "utf-8"
        env_file = ".env"


config = Config()
