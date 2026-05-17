import streamlit as st
import json
from llm import generate
from prompts import get_question_prompt, evaluate_answer_prompt

st.title("🎤 AI Interview Simulator")

# Session state
if "question" not in st.session_state:
    st.session_state.question = ""

if "history" not in st.session_state:
    st.session_state.history = []

# Inputs
role = st.selectbox("Role", ["Frontend Developer", "Backend Developer", "Data Analyst"])
level = st.selectbox("Level", ["Beginner", "Intermediate", "Advanced"])

# Generate question
if st.button("Start Interview"):
    prompt = get_question_prompt(role, level)
    st.session_state.question = generate(prompt)

# Show question
if st.session_state.question:
    st.subheader("Question")
    st.write(st.session_state.question)

    answer = st.text_area("Your Answer")

    if st.button("Submit Answer"):
        eval_prompt = evaluate_answer_prompt(st.session_state.question, answer)
        result = generate(eval_prompt)

        st.subheader("Evaluation")
        st.code(result)

        try:
            data = json.loads(result)

            st.write("Score:", data["score"])
            st.write("Feedback:", data["feedback"])
            st.write("Improvement:", data["improvement"])

            st.session_state.history.append({
                "q": st.session_state.question,
                "a": answer,
                "score": data["score"]
            })

        except:
            st.error("Invalid JSON response")

# History
st.sidebar.title("History")
for item in st.session_state.history:
    st.sidebar.write(f"Q: {item['q'][:30]}...")
    st.sidebar.write(f"Score: {item['score']}")