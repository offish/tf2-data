import json
import os


def get_json_path(name: str) -> str:
    return os.path.abspath(__file__).replace("utils.py", "") + f"/json/{name}.json"


def read_json_file(path: str) -> dict | list:
    data = {}

    with open(path, "r") as f:
        data = json.loads(f.read())

    return data


def read_lib_json_file(name: str) -> dict | list:
    path = get_json_path(name)
    return read_json_file(path)


def write_json_file(path: str, data: dict | list) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
