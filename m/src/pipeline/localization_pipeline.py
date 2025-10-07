import sys
from src.logger import logging
from src.exception import CustomException
from src.components.localizer import Localizer

class LocalizationPipeline:
    """Localization pipeline"""
    
    def __init__(self):
        self.localizer = Localizer()
    
    def localize(self, text: str, src_lang: str, tgt_lang: str, 
                currency: str = 'USD', units: str = 'metric') -> dict:
        """Execute localization"""
        try:
            result = self.localizer.full_localization(text, src_lang, tgt_lang, currency, units)
            result['success'] = True
            return result
        except Exception as e:
            logging.error(f"Localization error: {str(e)}")
            raise CustomException(e, sys)