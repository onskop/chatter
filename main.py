# First
import openai 
import streamlit as st
with st.sidebar:
    openai_api_key = st.secrets["openai_key"]

    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"


st.title("💬 Chatbor")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)


with st.sidebar:
    st.write(st.session_state.messages)