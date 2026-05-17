import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_response(prompt, temperature):
    try:
        response = model.generate_content(
            contents=prompt,
            generation_config={
                "temperature": temperature
            }
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"