import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# App title
st.title("LLM Chat Demo")

# Initialize chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# Display previous messages
for message in st.session_state.chat:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
prompt = st.chat_input("Ask something")

if prompt:
    # Add user message
    st.session_state.chat.append({"role": "user", "content": prompt})

    # Send request to Groq
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.chat
    )

    reply = response.choices[0].message.content

    # Add assistant reply
    st.session_state.chat.append({"role": "assistant", "content": reply})

    st.rerun()
