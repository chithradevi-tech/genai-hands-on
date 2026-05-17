from openai import OpenAI
from config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def get_response(messages):
    res = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )
    return res.choices[0].message.content