import sys
import pandas as pd
from tqdm import tqdm
from src.logger import logging
from src.exception import CustomException
from src.components.translator import Translator

class BatchProcessor:
    """Batch translation processor"""
    
    def __init__(self):
        self.translator = Translator()
    
    def process_list(self, texts: list, src_lang: str, tgt_lang: str) -> list:
        """Process list of texts"""
        try:
            translations = []
            for text in tqdm(texts, desc="Translating"):
                translation = self.translator.translate(text, src_lang, tgt_lang)
                translations.append(translation)
            return translations
        except Exception as e:
            raise CustomException(e, sys)
    
    def process_dataframe(self, df: pd.DataFrame, text_column: str, 
                         src_lang: str, tgt_lang: str) -> pd.DataFrame:
        """Process DataFrame"""
        try:
            translations = []
            for text in tqdm(df[text_column], desc="Translating"):
                translation = self.translator.translate(str(text), src_lang, tgt_lang)
                translations.append(translation)
            
            df['translation'] = translations
            df['source_lang'] = src_lang
            df['target_lang'] = tgt_lang
            return df
        except Exception as e:
            raise CustomException(e, sys)