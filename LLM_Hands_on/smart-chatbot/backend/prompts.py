def get_system_prompt(role):
    prompts = {
        "Teacher": "Explain clearly with examples.",
        "Friend": "Talk casually and friendly.",
        "Interviewer": "Ask tough questions and evaluate answers."
    }
    return prompts.get(role, "")