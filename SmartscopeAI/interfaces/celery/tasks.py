import json
from .app import app
from ...microservice.main import get_method, run_method


@app.task
def find_squares(data: str):
    result = run_method('find_squares',data)
    print(result)
    return result

@app.task
def find_holes(data: str):
    result = run_method('find_holes',data)
    print(result)
    return result
