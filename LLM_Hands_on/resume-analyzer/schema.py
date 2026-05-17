def get_prompt(resume_text):
    return f"""
You are a resume analyzer.

Extract structured information and return ONLY valid JSON.

Rules:
- No explanation
- No markdown
- No extra text

Format:
{{
  "name": "",
  "skills": [],
  "experience_summary": "",
  "score": 0,
  "improvements": []
}}

Resume:
{resume_text[:5000]}
"""