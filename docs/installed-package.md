# Packages

## Installed Packages

### utilities

```bash
python-dotenv
```

### langchain

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
```

### data process | analysis

```bash
poetry add pandas rank-bm25
```

### database | cache

```bash
poetry add redis
poetry add chromadb==0.5.23
```

## install できなかった packages

```bash
#  Installing torch (2.4.1): Failed
poetry add langchain-huggingface
# Downgrading tokenizers (0.21.0 -> 0.19.1): Failed
poetry add langchain-upstage
# Installing torch (1.13.1): Failed
poetry add langchain-teddynote
```

## ETC

```bash
# maintain 하지않으므로 install 하지 않음
poetry add langchainhub
```
