import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def detect_action(user_input):

    prompt = f"""
    Decide action.

    User: {user_input}

    Return ONLY one word:
    save
    retrieve
    delete
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip().lower()