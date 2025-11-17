import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SNOW_INSTANCE_URL = os.getenv("SNOW_INSTANCE_URL", "").rstrip("/")
SNOW_USERNAME = os.getenv("SNOW_USERNAME")
SNOW_PASSWORD = os.getenv("SNOW_PASSWORD")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
