import sys
import re
from src.logger import logging
from src.exception import CustomException
from src.components.translator import Translator

class Localizer:
    """Localization component"""
    
    def __init__(self):
        self.translator = Translator()
        self.currency_map = {'USD': '$', 'EUR': '€', 'GBP': '£', 'INR': '₹', 'JPY': '¥'}
    
    def localize_currency(self, text: str, target_currency: str = 'USD') -> str:
        """Convert currency symbols"""
        try:
            pattern = r'\$(\d+(?:\.\d{2})?)'
            symbol = self.currency_map.get(target_currency, '$')
            return re.sub(pattern, f'{symbol}\\1', text)
        except Exception as e:
            raise CustomException(e, sys)
    
    def localize_units(self, text: str, target_system: str = 'metric') -> str:
        """Convert units (miles to km, F to C)"""
        try:
            if target_system == 'metric':
                # Miles to Km
                text = re.sub(r'(\d+)\s*miles', lambda m: f"{int(m.group(1)) * 1.6:.1f} km", text)
                # F to C
                text = re.sub(r'(\d+)°F', lambda m: f"{(int(m.group(1)) - 32) * 5/9:.1f}°C", text)
            return text
        except Exception as e:
            raise CustomException(e, sys)
    
    def full_localization(self, text: str, src_lang: str, tgt_lang: str, 
                         currency: str = 'USD', units: str = 'metric') -> dict:
        """Complete localization"""
        try:
            # Translate
            translated = self.translator.translate(text, src_lang, tgt_lang)
            
            # Localize
            translated = self.localize_currency(translated, currency)
            translated = self.localize_units(translated, units)
            
            return {
                'original': text,
                'translated': translated,
                'source_lang': src_lang,
                'target_lang': tgt_lang,
                'currency': currency,
                'units': units
            }
        except Exception as e:
            raise CustomException(e, sys)