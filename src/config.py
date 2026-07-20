"""Shared configuration for CLI, API, and engines."""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


ROOT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT_DIR / "output"
FILINGS_DIR = ROOT_DIR / "data" / "filings"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    ollama_base_url: str = "http://127.0.0.1:11434"
    ollama_model: str = "llama3"
    sec_user_agent: str = "EquityResearchAgent local-dev@example.com"
    host: str = "0.0.0.0"
    port: int = 8000
    # Optional shared PIN for LAN access (empty = open on local network)
    access_pin: str = ""


settings = Settings()
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
FILINGS_DIR.mkdir(parents=True, exist_ok=True)
