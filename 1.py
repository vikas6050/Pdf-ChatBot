from Retrieval.core import run_llm
import streamlit as st
from streamlit_chat import message

st.header("LangChain Udemy Course- Documentation Helper Bot")

prompt = st.text_input("Prompt", placeholder="Enter your prompt here..")

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []

if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

def create_sources_string(source_documents: list) -> str:
    if not source_documents:
        return ""
    sources_string = ""
    for i, document in enumerate(source_documents):
        page_number = document.metadata.get("page", "")
        page_content = document.page_content
        sources_string += f"Page {page_number}:\n{page_content}\n---\n"
    return sources_string

if prompt:
    # Clear frontend before processing new prompt
    st.session_state["user_prompt_history"].clear()
    st.session_state["chat_answers_history"].clear()
    st.session_state["chat_history"].clear()

    with st.spinner("Generating response.."):
        generated_response = run_llm(
            query=prompt, chat_history=st.session_state["chat_history"]
        )
        source_documents = generated_response.get("source_documents", [])

        formatted_response = (
            f"Chatbot Response:\n{generated_response['answer']} \n\n"
            f"Source content:\n\n{create_sources_string(source_documents)}"
        )

        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(formatted_response)
        st.session_state["chat_history"].append((prompt, generated_response["answer"]))

if st.session_state["chat_answers_history"]:
    for index, (user_query, generated_response) in enumerate(zip(
        st.session_state["user_prompt_history"],
        st.session_state["chat_answers_history"],
    )):
        message(user_query, is_user=True, key=f"user_query_{index}")
        message(generated_response, key=f"generated_response_{index}")
