# MEMO

## Instruction

- `chain.invoke`

```python
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

prompt = PromptTemplate.from_template("{num} 의 10배는?")
llm = ChatOpenAI(temperature=0)

chain = prompt | llm
chain.invoke({"num": 5})
```

- `chain.stream`

```python
from langchain_core.output_parsers import StrOutputParser
from langchain_teddynote.messages import stream_response
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# template 정의
template = "{country}의 수도는 어디인가요?"

prompt = PromptTemplate(
    template=template,
    input_variables=["country"],
)

chain = prompt | ChatOpenAI(model_name="gpt-4o", temperature=0) | StrOutputParser()

answer = chain.stream({"country": "Korea"})
stream_response(answer)
```

## Chat

- `chat.invoke`

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
chat_template = ChatPromptTemplate.from_messages(
    [
        # role, message
        ("system", "당신은 친절한 AI 어시스턴트입니다. 당신의 이름은 {name} 입니다."),
        ("human", "반가워요!"),
        ("ai", "안녕하세요! 무엇을 도와드릴까요?"),
        ("human", "{user_input}"),
    ]
)

# 챗 message 를 생성합니다.
messages = chat_template.format_messages(
    name="테디", user_input="당신의 이름은 무엇입니까?"
)
# messages

## method 01
llm.invoke(messages).content

## method 02
chain = chat_template | llm
chain.invoke({"name": "Teddy", "user_input": "당신의 이름은 무엇입니까?"}).content
```

- `chat.predict_messages`

```python
from langchain.schema import HumanMessage, AIMessage, SystemMessage

messages = [
    SystemMessage(
        content="You are a geography expert. And you only reply in Italian.",
    ),
    AIMessage(content="Ciao, mi chiamo colas!"),
    HumanMessage(
        content="What is the distance between Tailand and Korea. Also, what is your name?",
    ),
]

chat = ChatOpenAI(temperature=0.1)
chat.predict_messages(messages)
```

- `chat.predict`

```python
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.prompts import PromptTemplate, ChatPromptTemplate

chat = ChatOpenAI(temperature=0.1)
template = PromptTemplate.from_template("What is the distance between {country_a} and {country_b}.")
promtp = template.format(country_a="Italy", country_b="France")

chat.predict(promtp)
```
