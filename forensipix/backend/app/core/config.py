from pydantic import ConfigDict
from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "ForensiPix"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Database - use SQLite for development, PostgreSQL for production
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./forensipix.db")
    
    # Security
    SECRET_KEY: str = "your-secret-key-here"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # Storage
    STORAGE_PATH: str = "./storage"
    MAX_UPLOAD_SIZE_MB: int = 50
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:5173", "http://localhost:3000"]
    
    # AI Model
    AI_MODEL_PATH: str = ""
    
    model_config = ConfigDict(env_file=".env", case_sensitive=False)

settings = Settings()
