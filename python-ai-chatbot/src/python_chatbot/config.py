import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("GROQ_MODEL")

if not groq_api_key:
    raise ValueError("API Key is not found!")

if not model:
    raise ValueError("Model is not found!")