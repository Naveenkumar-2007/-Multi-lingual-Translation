import os
from dataclasses import dataclass

@dataclass
class ModelConfig:
    """Model configuration"""
    
    ARTIFACTS_DIR: str = "artifacts"
    MODELS_DIR: str = "artifacts/models"
    CACHE_DIR: str = "artifacts/cache"
    
    MBART_MODEL: str = "facebook/mbart-large-50-many-to-many-mmt"
    
    MAX_LENGTH: int = 512
    NUM_BEAMS: int = 5
    
    SUPPORTED_LANGUAGES = ['en', 'es', 'fr', 'de', 'hi', 'zh', 'ar', 'ru', 'ja', 'te']
    LANGUAGE_CODES = {
        'en': 'en_XX',
        'es': 'es_XX',
        'fr': 'fr_XX',
        'de': 'de_DE',
        'hi': 'hi_IN',
        'zh': 'zh_CN',
        'ar': 'ar_AR',
        'ru': 'ru_RU',
        'ja': 'ja_XX',
        'te': 'te_IN'  
    }
