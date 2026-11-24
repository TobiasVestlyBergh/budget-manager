import json
from pathlib import Path


def load_transactions(path):
    if not Path(path).exists():
        return []

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_transactions(transactions, path):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(transactions, file, indent=2)
