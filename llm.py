import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def should_create_ticket(user_question: str) -> bool:
    prompt = f"""
You are a customer support AI.

User question:
"{user_question}"

The system could not find an answer in internal documents.

Answer ONLY one word:
YES - if a support ticket should be created
NO - if not needed
"""

    try:
        r = requests.post(
            OPENROUTER_URL,
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "openai/gpt-4o-mini",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0,
                "max_tokens": 5
            },
            timeout=20
        )

        r.raise_for_status()
        data = r.json()

        text = data["choices"][0]["message"]["content"].strip().upper()

        return text.startswith("YES")

    except Exception as e:
        print("Ticket decision error:", e)
        # В случае ошибки НЕ создаём тикет автоматически
        return False


def answer_general_question(question: str) -> str:
    prompt = f"""
You are a professional customer support assistant.

Answer the following question clearly and professionally.
Do NOT invent document references.
If the question is vague, explain possible interpretations.

Question:
{question}
"""

    try:
        r = requests.post(
            OPENROUTER_URL,
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "openai/gpt-4o-mini",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.2,
                "max_tokens": 500
            },
            timeout=20
        )

        r.raise_for_status()
        data = r.json()

        return data["choices"][0]["message"]["content"].strip()

    except Exception as e:
        print("General answer error:", e)
        return "⚠️ Sorry, I couldn't generate an answer right now. Please try again."
