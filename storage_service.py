import os
from pathlib import Path

BASE_DIR = Path("storage/images")

BASE_DIR.mkdir(parents=True, exist_ok=True)


def save_file_locally(file_obj, filename: str):
    file_path = BASE_DIR / filename

    with open(file_path, "wb") as buffer:
        buffer.write(file_obj.read())

    return str(file_path)
