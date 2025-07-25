import os
from typing import Optional
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings(BaseSettings):
    # API Keys
    openai_api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
    anthropic_api_key: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    google_api_key: Optional[str] = os.getenv("GOOGLE_API_KEY")
    azure_api_key: Optional[str] = os.getenv("AZURE_API_KEY")
    azure_api_base: Optional[str] = os.getenv("AZURE_API_BASE")
    azure_api_version: Optional[str] = os.getenv("AZURE_API_VERSION")
    aws_access_key_id: Optional[str] = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key: Optional[str] = os.getenv("AWS_SECRET_ACCESS_KEY")
    aws_region_name: Optional[str] = os.getenv("AWS_REGION_NAME", "us-east-1")
    cohere_api_key: Optional[str] = os.getenv("COHERE_API_KEY")
    replicate_api_key: Optional[str] = os.getenv("REPLICATE_API_KEY")
    huggingface_api_key: Optional[str] = os.getenv("HUGGINGFACE_API_KEY")
    
    # Default settings
    default_model: str = os.getenv("DEFAULT_MODEL", "gpt-3.5-turbo")
    
    # Server settings
    port: int = int(os.getenv("PORT", "8000"))
    host: str = os.getenv("HOST", "0.0.0.0")
    
    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "ignore"  # Ignore extra fields

# Create settings instance
settings = Settings()

# Configure LiteLLM with available API keys
import litellm

if settings.openai_api_key:
    os.environ["OPENAI_API_KEY"] = settings.openai_api_key

if settings.anthropic_api_key:
    os.environ["ANTHROPIC_API_KEY"] = settings.anthropic_api_key

if settings.google_api_key:
    os.environ["GOOGLE_API_KEY"] = settings.google_api_key

if settings.azure_api_key:
    os.environ["AZURE_API_KEY"] = settings.azure_api_key
    if settings.azure_api_base:
        os.environ["AZURE_API_BASE"] = settings.azure_api_base
    if settings.azure_api_version:
        os.environ["AZURE_API_VERSION"] = settings.azure_api_version

if settings.aws_access_key_id and settings.aws_secret_access_key:
    os.environ["AWS_ACCESS_KEY_ID"] = settings.aws_access_key_id
    os.environ["AWS_SECRET_ACCESS_KEY"] = settings.aws_secret_access_key
    os.environ["AWS_REGION_NAME"] = settings.aws_region_name

if settings.cohere_api_key:
    os.environ["COHERE_API_KEY"] = settings.cohere_api_key

if settings.replicate_api_key:
    os.environ["REPLICATE_API_KEY"] = settings.replicate_api_key

if settings.huggingface_api_key:
    os.environ["HUGGINGFACE_API_KEY"] = settings.huggingface_api_key

# Set verbose mode for debugging (optional)
litellm.set_verbose = False