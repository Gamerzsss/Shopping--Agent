# config.py
import os
from dotenv import load_dotenv

load_dotenv()

def get_gemini_api_key():
    return os.getenv("GEMINI_API_KEY")

def get_tavily_api_key():
    return os.getenv("TAVILY_API_KEY")

if __name__ == "__main__":
    print(get_gemini_api_key())
    print(get_tavily_api_key())