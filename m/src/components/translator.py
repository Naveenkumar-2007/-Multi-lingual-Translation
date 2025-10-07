import sys
import torch
from src.logger import logging
from src.exception import CustomException
from src.components.model_loader import model_load
from config.model_config import ModelConfig

class Translator:
    """Translation component"""
    
    def __init__(self):
        self.model_loader = model_load()
        self.config = ModelConfig()
        self.model_loader.load_mbart()
    
    def translate(self, text: str, src_lang: str, tgt_lang: str) -> str:
        """
        Translate text
        
        Args:
            text: Input text
            src_lang: Source language (e.g., 'en')
            tgt_lang: Target language (e.g., 'es')
        
        Returns:
            Translated text
        """
        try:
            model, tokenizer = self.model_loader.model_load()
            
            # Get language codes
            src_code = self.config.LANGUAGE_CODES.get(src_lang, 'en_XX')
            tgt_code = self.config.LANGUAGE_CODES.get(tgt_lang, 'es_XX')
            
            # Set source language
            tokenizer.src_lang = src_code
            
            # Encode
            encoded = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
            
            # Generate translation
            with torch.no_grad():
                generated = model.generate(
                    **encoded,
                    forced_bos_token_id=tokenizer.lang_code_to_id[tgt_code],
                    max_length=512,
                    num_beams=5
                )
            
            # Decode
            translation = tokenizer.batch_decode(generated, skip_special_tokens=True)[0]
            
            logging.info(f"Translated: {src_lang} -> {tgt_lang}")
            return translation
        
        except Exception as e:
            logging.error(f"Translation error: {str(e)}")
            raise CustomException(e, sys)