import google.generativeai as genai
from config import API_KEY, MODEL

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(MODEL)

def clean_json(text):
    text = text.replace("```json", "").replace("```", "")
    return text.strip()

def analyze_resume(prompt):
    try:
        response = model.generate_content(
            contents=prompt,
            generation_config={
                "temperature": 0.3  # low for structured output
            }
        )
        return clean_json(response.text)
    except Exception as e:
        return f"Error: {str(e)}"