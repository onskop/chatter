# streamlit run "c:\Users\oskop\OneDrive - Novavax Inc\Production dev\PyProj\AI\novabot\llama.py"

import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader


openai.api_key = st.secrets.openai_key
st.header("Chat with Novavax docs 💬 📚")

if "messages" not in st.session_state.keys(): # Initialize the chat message history
    st.session_state.messages = [
        {"role": "system", "content": "Welcome to the Novavax docs chat!"},
        {"role": "assistant", "content": "Ask me a question about our plentiful documentation and SOPs!"}
    ]

@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing the docs – hang tight! This should take 1-2 minutes."):
        reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert pharmaceutical process specialist and your job is to answer technical questions. Assume that all questions are related to Novavax process documentation library. Keep your answers technical and based on facts – do not hallucinate features."))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

index = load_data()

with st.sidebar:
    st.radio("Chat mode", ["simple", "best", "context", "condense_question"], key="chat_mode")
    st.write("For more information on the chat modes, see the [documentation] - https://gpt-index.readthedocs.io/en/stable/core_modules/query_modules/chat_engines/usage_pattern.html#configuring-a-chat-engine")


chat_engine = index.as_chat_engine(chat_mode=st.session_state['chat_mode'], verbose=True) #context condense_question
if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history