import streamlit as st
from llm import generate_response
from utils import save_prompt, load_prompts

st.set_page_config(page_title="Prompt Playground")

st.title("🧠 Prompt Playground (Free LLM)")

# INPUT
prompt = st.text_area("Enter your prompt")

temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
num_outputs = st.selectbox("Outputs", [1, 2, 3])

# GENERATE
if st.button("Generate"):
    if prompt:
        cols = st.columns(num_outputs)

        for i in range(num_outputs):
            with cols[i]:
                st.markdown(f"### Output {i+1}")
                res = generate_response(prompt, temperature)
                st.write(res)

# SAVE
if st.button("Save Prompt"):
    if prompt:
        save_prompt(prompt)
        st.success("Saved!")

# SIDEBAR
st.sidebar.title("Saved Prompts")
saved = load_prompts()

for p in saved:
    if st.sidebar.button(p):
        st.session_state["selected"] = p

if "selected" in st.session_state:
    st.text_area("Selected Prompt", st.session_state["selected"])