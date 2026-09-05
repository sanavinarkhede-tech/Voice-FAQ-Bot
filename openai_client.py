import os
from dotenv import load_dotenv
from google import genai

load_dotenv(override=True)

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing in .env file")

client = genai.Client(api_key=API_KEY)

GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite")