from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini",
    google_api_key = os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)