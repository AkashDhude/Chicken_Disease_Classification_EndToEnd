import os
from box.exceptions import BoxValueError
import yaml
from ChickenDiseaseClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object

    Args: 
    path_to_yaml(str): Path to the yaml file

    Raises:
    BoxValueError: If the yaml file does not exist


    Return: ConfigBox object
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    """
    Create list of directories

    Args:
        path_to_directories(list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Default is False

    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"{path} created successfully")


@ensure_annotations
def save_json(path:Path, data:dict):
    """
    Save json file 
    
    Args:
    path(Path): Path to the json file
    data(dict): Data to be saved in json file

    """
    with open(path, 'w') as f:
            json.dump(data, f, indent=4)
    
    logger.info(f"{path} saved successfully")


@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """
    Load json file 
    
    Args:
    path(Path): Path to the json file

    Returns:
    ConfigBox: ConfigBox type
    """
    with open(path) as f:
        data = json.load(f)

    logger.info(f"{path} loaded successfully")
    return ConfigBox(data)


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()
        
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())

