import os
import sys
import pickle
import yaml
import json
from pathlib import Path
from typing import Any, Dict, List
import pandas as pd
from src.exception import CustomException
from src.logger import logging

def save_object(file_path: str, obj: Any) -> None:
    """
    Save Python object as pickle file
    
    Args:
        file_path: Path to save the object
        obj: Object to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        
        logging.info(f"Object saved successfully at {file_path}")
    
    except Exception as e:
        logging.error(f"Error saving object: {str(e)}")
        raise CustomException(e, sys)

def load_object(file_path: str) -> Any:
    """
    Load pickle object from file
    
    Args:
        file_path: Path to the pickle file
    
    Returns:
        Loaded object
    """
    try:
        with open(file_path, "rb") as file_obj:
            obj = pickle.load(file_obj)
        
        logging.info(f"Object loaded successfully from {file_path}")
        return obj
    
    except Exception as e:
        logging.error(f"Error loading object: {str(e)}")
        raise CustomException(e, sys)

def load_config(config_path: str = "config/config.yaml") -> Dict:
    """
    Load configuration from YAML file
    
    Args:
        config_path: Path to config file
    
    Returns:
        Configuration dictionary
    """
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        
        logging.info(f"Configuration loaded from {config_path}")
        return config
    
    except Exception as e:
        logging.error(f"Error loading config: {str(e)}")
        raise CustomException(e, sys)

def save_json(file_path: str, data: Dict) -> None:
    """
    Save dictionary as JSON file
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        logging.info(f"JSON saved at {file_path}")
    
    except Exception as e:
        logging.error(f"Error saving JSON: {str(e)}")
        raise CustomException(e, sys)

def load_json(file_path: str) -> Dict:
    """
    Load JSON file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        logging.info(f"JSON loaded from {file_path}")
        return data
    
    except Exception as e:
        logging.error(f"Error loading JSON: {str(e)}")
        raise CustomException(e, sys)

def create_directories(dirs: List[str]) -> None:
    """
    Create multiple directories
    """
    try:
        for dir_path in dirs:
            os.makedirs(dir_path, exist_ok=True)
            logging.info(f"Directory created: {dir_path}")
    
    except Exception as e:
        logging.error(f"Error creating directories: {str(e)}")
        raise CustomException(e, sys)

def get_file_size(file_path: str) -> str:
    """
    Get human-readable file size
    """
    try:
        size_bytes = os.path.getsize(file_path)
        
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        
        return f"{size_bytes:.2f} TB"
    
    except Exception as e:
        logging.error(f"Error getting file size: {str(e)}")
        raise CustomException(e, sys)