import json
import hashlib


def load_data(path: str):
    with open(path) as file:
        data = json.load(file)
    return data


def refactor_url_for_key(url_str):
    words = url_str.split('_')
    key = ' '.join([word.title() for word in words])
    return key


def json_md5_hash(json_data) -> str:
    if type(json_data) == dict:
        json_data = json.dumps(json_data)
    md5_hash = hashlib.md5(json_data.encode("UTF-8")).hexdigest()
    return md5_hash


def compare_json_md5_hash(json_request: str, json_file_path: str) -> bool:
    with open(json_file_path, 'r', encoding='utf-8') as file:
        json_file_contents = json.dumps(json.load(file))
    request_md5 = json_md5_hash(json_request)
    file_md5 = json_md5_hash(json_file_contents)
    return request_md5 == file_md5


def format_json(json_like_str: str) -> str:
    json_str = json_like_str.replace("'", '"')
    python_obj = json.loads(json_str)
    formatted_json_str = json.dumps(python_obj, ensure_ascii=False)
    return formatted_json_str
