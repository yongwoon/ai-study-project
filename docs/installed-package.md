# Packages

## Installed Packages

### utilities

```bash
python-dotenv
```

### langchain

```bash
# LLM 제공자 관련 패키지
poetry add huggingface-hub openai deepl kiwipiepy konlpy

# 핵심 패키지 먼저 설치
poetry add langchain langchain-core

# 기본 확장 패키지
poetry add langchain-experimental langchain-community

# LLM 제공자 관련 langchain 패키지
poetry add langchain-openai langchain-anthropic langchain-cohere

# Vector Store 관련 패키지
poetry add langchain-elasticsearch langchain-chroma langchain-milvus

# 기타 통합 패키지
poetry add langchain-google langchain-huggingface langchain-upstage langchain-teddynote
```

### data process and analysis

```bash
poetry add pandas rank-bm25
```

### database and cache

```bash
poetry add redis
poetry add chromadb==0.5.23
```

### pdf and file process

```bash
poetry add pymupdf
poetry add pypdf
poetry add pdfplumber
poetry add pdfminer-six=20231228
poetry add pymupdf4llm
```

### visualize and user interface

```bash
poetry add matplotlib streamlit jupyter notebook
```

### deep learning and machine learning

```bash
poetry add torch torchvision faiss-cpu open-clip-torch
```

### Utils

```bash
poetry add python-dotenv pydantic lxml pillow lark ragas
poetry add "unstructured[all-docs]"
poetry add arxiv tiktoken tenacity pymilvus google-search-results protobuf sqlalchemy llama-index-core llama-parse  flashrank docx2txt nest-asyncio rapidocr-onnxruntime seaborn grandalf rouge-score langchain-ollama mypy pinecone wikipedia scikit-learn
```

## ETC

```bash
# maintain 하지않으므로 install 하지 않음
poetry add langchainhub
```

## install 하지 않은 패키지

```bash
# langchain-teddynote 의 코드를 사용하지 않고 코드를 작성할 예정이므로 install 하지 않음
poetry add langchain-teddynote
# depends on both pypdf (>=4.3.1,<5.0.0) 문제도 일단 무시
poetry add llama-index-readers-file

```
