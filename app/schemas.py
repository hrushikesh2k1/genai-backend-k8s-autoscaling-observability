from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str

class GenAIResponse(BaseModel):
    response: str
