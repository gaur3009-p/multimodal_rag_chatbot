# frontend/app.py
import streamlit as st
import requests
import base64
import uuid

st.title("Multimodal Chat Assistant")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
user_input = st.text_input("Your message", placeholder="Type your question...")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if uploaded_file or user_input:
    image_b64 = base64.b64encode(uploaded_file.read()).decode() if uploaded_file else None
    user_message = user_input or "What can you tell me about this image?"
    
    st.session_state.messages.append({"role": "user", "content": user_message})
    if uploaded_file:
        st.session_state.messages.append({"role": "user", "content": "Uploaded image"})
    
    response = requests.post(
        "http://localhost:8000/chat",
        json={
            "message": user_message,
            "image": image_b64,
            "session_id": st.session_state.session_id
        }
    ).json()
    
    st.session_state.messages.append({"role": "assistant", "content": response['response']})
    
    st.rerun()
