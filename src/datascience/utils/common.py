import os
import sys
import yaml
import json
import joblib
from pathlib import Path
from box import ConfigBox
from typing import Any
from box.exceptions import BoxValueError

from src.datascience import logger


def read_yaml(path_to_yaml) -> ConfigBox:
    """
    read yaml file and return

    Args: path_to_yaml (str): Path like input

    Raises: ValueError: If Yaml file is empty
    
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Yaml File: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e


def create_directories(path_to_direcories: list, verbose=True):
    """
    Create a list of directoryes

    Args: Path to directories (list): list of paths of directories
    ignore_log (bool,option): ignore if multiple dirs is to be created

    """
    for path in path_to_direcories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


def save_json(path: Path, data:dict):
    """"
    Save Json data

    Args:
        path (Path): Path to json file
        data (dict): data to be saved in Json file

    """
    with open(path,'w') as file_obj:
        json.dump(data,file_obj,indent=4)

    logger.info(f"Json file save at: {path}")


def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)
    logger.info("Json file loaded succesfully")

    return ConfigBox(content)

def save_bin(data: Any, path: Path):
    """
    save binary file

    Args:
        data (Any) : data to be saved as binary
        path (Path) : path to binary file

    """

    joblib.dump(value=data,filename=path)
    logger.info(f"Saved Binary file at {path}")


def load_bin(path: Path):
    data = joblib.load(path)
    logger.info(f"Binary file loaded from {path}")
    return data
                


            
