from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from src.pipeline.translation_pipeline import TranslationPipeline
from src.pipeline.localization_pipeline import LocalizationPipeline

app = FastAPI(
    title="Multi-lingual Translator API",
    description="Translation & Localization API",
    version="1.0.0"
)

# Load pipelines
trans_pipeline = TranslationPipeline()
local_pipeline = LocalizationPipeline()

# Request models
class TranslationRequest(BaseModel):
    text: str
    source_lang: str
    target_lang: str

class LocalizationRequest(BaseModel):
    text: str
    source_lang: str
    target_lang: str
    currency: Optional[str] = 'USD'
    units: Optional[str] = 'metric'

@app.get("/")
def home():
    return {"message": "Welcome to Multi-lingual Translator API", "status": "active"}

@app.post("/translate")
def translate(request: TranslationRequest):
    """Simple translation endpoint"""
    try:
        result = trans_pipeline.translate(
            request.text,
            request.source_lang,
            request.target_lang
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/localize")
def localize(request: LocalizationRequest):
    """Translation with localization endpoint"""
    try:
        result = local_pipeline.localize(
            request.text,
            request.source_lang,
            request.target_lang,
            request.currency,
            request.units
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/languages")
def get_languages():
    """Get supported languages"""
    return {
        "supported_languages": ['en', 'es', 'fr', 'de', 'hi', 'zh', 'ar', 'ru', 'ja','te']
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)