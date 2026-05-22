import os

def read_file(path: str) -> str:
    if not os.path.exists(path):
        raise ValueError("Must provide valid path")
    with open(path, 'r') as f:
        return f.read()
    