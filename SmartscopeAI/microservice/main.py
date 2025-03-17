from pydantic import BaseModel
from .data import METHODS_MAPPING

def get_method(method:str) -> BaseModel:
    method = METHODS_MAPPING.get(method, None)
    if method is None:
        raise ValueError(f'Method {method} not found')
    return method

def run_method(method:str, data:dict):
    method: BaseModel = get_method(method)
    method = method.model_validate_json(data)
    return method.method(image=method.image, **method.kwargs.dict())