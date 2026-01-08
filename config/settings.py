import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    # Project Paths
    BASE_DIR = Path(__file__).resolve().parent.parent
    OUTPUT_DIR = BASE_DIR / "output"

    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    AI_MODEL = os.getenv("AI_MODEL_NAME", "gpt-4o-mini")
    AI_TEMPERATURE = float(os.getenv("AI_TEMPERATURE", "0.2"))
    AI_MAX_TOKENS = int(os.getenv("AI_MAX_TOKENS", "4000"))

    # Scraper Configuration
    HEADLESS = os.getenv("HEADLESS_MODE", "True").lower() == "true"
    TIMEOUT = int(os.getenv("SCRAPE_TIMEOUT", "30000"))

    def validate(self):
        """Ensure critical variables are set."""
        if not self.OPENAI_API_KEY:
            raise ValueError("Missing OPENAI_API_KEY in .env file.")

# Create a global settings instance
settings = Settings()