def get_question_prompt(role, level):
    return f"""
You are an interviewer.

Generate ONE interview question.

Role: {role}
Level: {level}

Only return the question.
"""


def evaluate_answer_prompt(question, answer):
    return f"""
You are an interviewer.

Evaluate the candidate's answer.

Question:
{question}

Answer:
{answer}

Return JSON only:

{{
  "score": 0,
  "feedback": "",
  "improvement": ""
}}
"""