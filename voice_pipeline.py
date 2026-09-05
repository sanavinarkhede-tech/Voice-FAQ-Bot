import json
import os
import uuid

from app.services.openai_client import client, GEMINI_MODEL

FAQ_FILE = "data/faqs.json"
AUDIO_DIR = "data/audio"

os.makedirs(AUDIO_DIR, exist_ok=True)


def load_faqs():
    with open(FAQ_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def create_faq_context():
    faqs = load_faqs()

    context = ""

    for faq in faqs:
        context += f"""
Question: {faq["question"]}
Answer: {faq["answer"]}
"""

    return context


def ask_llm(question):
    faq_context = create_faq_context()

    prompt = f"""
You are a helpful College FAQ Voice Assistant.

Answer the user's question using ONLY the FAQ information below.

If the answer is not available in the FAQs, say:
"Sorry, I don't have information about that."

Keep the answer short, clear and friendly.

FAQ INFORMATION:
{faq_context}

USER QUESTION:
{question}
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text


def process_text(question):
    answer = ask_llm(question)

    return {
        "question": question,
        "answer": answer,
        "audio": None
    }


def process_voice(audio_data, original_filename):
    return {
        "question": "Voice input",
        "answer": "Voice processing will be added next.",
        "audio": None
    }