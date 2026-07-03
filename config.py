import os
from dataclasses import dataclass

@dataclass
class Config:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "your-api-key")
    MODEL_NAME: str = "gpt-4o"
    DB_CONNECTION_STRING: str = os.getenv("DB_CONNECTION_STRING", "sqlite:///retail_data.db")

config = Config()