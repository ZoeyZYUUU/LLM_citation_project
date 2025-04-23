import os
import cohere
from dotenv import load_dotenv

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def ask_cohere(prompt: str) -> str:
    try:
        response = co.chat(
            model="command-r",
            message=prompt,
            temperature=0.5,
            max_tokens=400
        )
        return response.text.strip()
    except Exception as e:
        return f"[Cohere Error] {e}"


