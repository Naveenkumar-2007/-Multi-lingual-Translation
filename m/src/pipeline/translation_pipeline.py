import sys
from src.logger import logging
from src.exception import CustomException
from src.components.translator import Translator

class TranslationPipeline:
    """Translation pipeline"""
    
    def __init__(self):
        self.translator = Translator()
    
    def translate(self, text: str, src_lang: str, tgt_lang: str) -> dict:
        """Execute translation"""
        try:
            translated = self.translator.translate(text, src_lang, tgt_lang)
            
            return {
                'success': True,
                'original': text,
                'translated': translated,
                'source_lang': src_lang,
                'target_lang': tgt_lang
            }
        except Exception as e:
            logging.error(f"Pipeline error: {str(e)}")
            raise CustomException(e, sys)