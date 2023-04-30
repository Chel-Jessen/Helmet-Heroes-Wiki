import json


def load_data(path: str):
    with open(path) as file:
        data = json.load(file)
    return data
