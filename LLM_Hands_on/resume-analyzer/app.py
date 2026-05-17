import streamlit as st
import json
from parser import extract_text
from schema import get_prompt
from llm import analyze_resume

st.title("📄 Resume Analyzer (LLM)")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    text = extract_text(uploaded_file)

    if st.button("Analyze Resume"):
        prompt = get_prompt(text)
        response = analyze_resume(prompt)

        st.subheader("Raw Output")
        st.code(response)

        try:
            data = json.loads(response)

            st.subheader("📊 Analysis")

            st.write("**Name:**", data.get("name"))
            st.write("**Score:**", data.get("score"))

            st.write("**Skills:**")
            st.write(data.get("skills"))

            st.write("**Experience Summary:**")
            st.write(data.get("experience_summary"))

            st.write("**Improvements:**")
            for imp in data.get("improvements", []):
                st.write("-", imp)

        except:
            st.error("Failed to parse JSON. Improve prompt.")