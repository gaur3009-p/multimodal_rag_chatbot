# Multimodal RAG Chatbot

A ChatGPT-like interface supporting text+image inputs with retrieval-augmented generation.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start services:

```bash
docker run -d -p 6379:6379 redis
docker run -d -p 8080:8080 cr.weaviate.io/semitechnologies/weaviate:1.22.4
```

3. Run the application:

```bash
uvicorn backend.main:app --reload
streamlit run frontend/app.py
```
