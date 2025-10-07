import sys
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from src.logger import logging
from src.exception import CustomException
from config.model_config import ModelConfig

class model_load:
    def __init__(self):
        self.config=ModelConfig
        self.model=None
        self.tokenizer=None
    def load_mbart(self):
        try:
            if self.model is None:
                logging.info(self.config.MBART_MODEL)
                self.model=MBartForConditionalGeneration.from_pretrained(
                    self.config.MBART_MODEL,
                    cache_dir=self.config.MODELS_DIR
                )
                self.token=MBart50TokenizerFast.from_pretrained(
                    self.config.MBART_MODEL,
                    cache_dir=self.config.MODELS_DIR

                )
        except Exception as ex:
            raise CustomException(ex,sys)
    def model_load(self):
        "loadmodel"
        if self.model is None:
            self.load_mbart()
        return self.model,self.token
        
