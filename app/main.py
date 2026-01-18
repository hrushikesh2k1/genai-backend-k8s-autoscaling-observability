from fastapi import FastAPI, HTTPException
from app.schemas import PromptRequest, GenAIResponse
from app.config import USE_MOCK_GENAI
from app.mock_genai import generate_text

app = FastAPI(title="GenAI Inference Service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate", response_model=GenAIResponse)
def generate(request: PromptRequest):
    try:
        response = generate_text(request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
