import streamlit as st
import openai

st.title("HexSoftwares AI Chatbot")

# Paste your OpenAI API key below
openai.api_key = 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

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Chat input UI
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # Get response from ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").markdown(reply)
