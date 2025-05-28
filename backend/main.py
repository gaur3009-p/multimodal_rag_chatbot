from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import base64
from rag_engine import RAGEngine
from memory import ConversationMemory
import uuid

app = FastAPI()
rag_engine = RAGEngine()
memory = ConversationMemory()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    image: str = None  
    session_id: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        image_data = base64.b64decode(request.image) if request.image else None
        response = rag_engine.generate_response(
            message=request.message,
            image=image_data,
            session_id=request.session_id
        )
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        content = await file.read()
        rag_engine.add_to_knowledge_base(content, file.filename)
        return {"status": "Document processed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.on_event("startup")
async def startup_event():
    rag_engine.initialize_components()
