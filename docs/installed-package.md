# Installed Package

## utilities

```bash
python-dotenv
```

## langchain

```bash
# 핵심 패키지 먼저 설치
poetry add langchain langchain-core

# 기본 확장 패키지
poetry add langchain-experimental langchain-community

# LLM 제공자 관련 패키지
poetry add huggingface-hub openai deepl kiwipiepy konlpy

# LLM 제공자 관련 langchain 패키지
poetry add langchain-openai langchain-anthropic langchain-cohere

# Vector Store 관련 패키지
poetry add langchain-elasticsearch langchain-chroma langchain-milvus

# 기타 통합 패키지
poetry add langchain-google
poetry add langchain-huggingface
poetry add langchain-upstage
poetry add langchain-teddynote
poetry add langchainhub
```
