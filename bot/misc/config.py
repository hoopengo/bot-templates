from pydantic import BaseSettings, Field


class Config(BaseSettings):
    TOKEN: str = Field(env="TOKEN", default="No token provided!")
    CMD_PREFIX: str = "."

    class Config:
        case_sensitive = False
        env_prefix = ""
        env_file_encoding = "utf-8"
        env_file = ".env"


config = Config()
