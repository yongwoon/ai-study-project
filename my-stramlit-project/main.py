import streamlit as st
from langchain_core.messages.chat import ChatMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
st.title("My LLM(Large Language Models) App")

# 처음 1 번만 실행하기 위한 코드
if "messages" not in st.session_state:
    # session: 대화 내용을 저장하기 위한 용도로 생성
    # @see https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state
    st.session_state["messages"] = []

with st.sidebar:
    clear_btn = st.button("Init chat")

def print_messages():
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message.role).write(chat_message.content)

def add_message(role: str, message: str):
    st.session_state["messages"].append(ChatMessage(role=role, content=message))

def create_chain():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("user", "#Question: \n{question}"),
    ])
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    chain = prompt | llm | StrOutputParser()

    return chain


# ========= Clear chat history =========
if clear_btn:
    st.session_state["messages"] = []

print_messages()

# ========= User Input =========
user_input = st.chat_input("Ask something")
if user_input:
    # Print User Input
    st.chat_message("user").write(user_input)

    chain = create_chain()
    response = chain.stream({"question": user_input})
    with st.chat_message("assistant"):
        container = st.empty()
        ai_answer = ""
        for token in response:
            ai_answer += token
            container.write(ai_answer)

    # Add User Input to Session
    add_message("user", user_input)
    add_message("assistant", ai_answer)

