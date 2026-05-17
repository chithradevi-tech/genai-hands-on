import json
import os

FILE = "prompts.json"

def save_prompt(prompt):
    data = []
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)

    data.append(prompt)

    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)


def load_prompts():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        return json.load(f)