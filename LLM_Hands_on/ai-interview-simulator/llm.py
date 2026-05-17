import google.generativeai as genai
from config import API_KEY, MODEL

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(MODEL)

def generate(text):
    try:
        res = model.generate_content(
            contents=text,
            generation_config={"temperature": 0.5}
        )
        return res.text
    except Exception as e:
        return f"Error: {str(e)}"