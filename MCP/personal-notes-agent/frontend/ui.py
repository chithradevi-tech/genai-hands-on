import streamlit as st
import requests

st.title("Personal Notes Agent")

message = st.text_input("Ask something")

if st.button("Send"):

    response = requests.post(
        "http://127.0.0.1:8000/chat",
        params={"user_input": message}
    )

    st.write("STATUS:", response.status_code)
    st.write("RAW RESPONSE:", response.text)

    try:
        st.write("JSON:", response.json())
    except Exception as e:
        st.error(f"Not JSON response: {e}")