from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# .env 位于本文件所在目录，避免因运行时工作目录不同而找不到配置
ENV_FILE = Path(__file__).resolve().parent / ".env"


class Settings(BaseSettings):
  model_config = SettingsConfigDict(env_file=ENV_FILE, env_file_encoding="utf-8")
  database_url: str

settings = Settings()