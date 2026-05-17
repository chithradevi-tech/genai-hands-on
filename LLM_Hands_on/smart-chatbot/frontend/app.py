import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.title("🤖 Smart Chatbot")

role = st.sidebar.selectbox(
    "Choose Role",
    ["Teacher", "Friend", "Interviewer"]
)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    payload = {
        "role": role,
        "messages": st.session_state.messages
    }

    res = requests.post(API_URL, json=payload)
    reply = res.json()["response"]

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)