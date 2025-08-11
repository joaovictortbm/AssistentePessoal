import streamlit as st
from chatbot import ask_question


st.set_page_config(
    page_title="Assistente pessoal",
    page_icon=":robot:",
)
st.markdown("<h1 style='text-align: center;'>Assistente pessoal</h1>",
            unsafe_allow_html=True)


if 'messages' not in st.session_state:
    st.session_state['messages'] = []

for message in st.session_state.messages:
    st.chat_message(message['role']).write(message['content'])

question = st.chat_input("Como posso ajudar?")

if question:
    st.chat_message("user").write(question)
    st.session_state.messages.append({"role": "user", "content": question})
    with st.spinner("Consultando banco de dados"):
        response = ask_question(question, st.session_state.messages)
        st.chat_message("ai").write(response)
        st.session_state.messages.append({"role": "ai", "content": response})
