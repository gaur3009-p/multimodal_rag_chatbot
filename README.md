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

# FuLl ImPlEmEnTaTiOn


This implementation provides a complete working foundation for a multimodal RAG chatbot. You'll need to:

1. Install Tesseract OCR for image processing (`apt-get install tesseract-ocr` on Ubuntu)
2. Configure proper model weights storage (models will auto-download)
3. Adjust the Weaviate schema and retrieval parameters based on your use case
4. Add error handling and logging for production use
5. Implement rate limiting and security measures

The system currently uses CPU-only inference - consider adding GPU support and model quantization for better performance.
