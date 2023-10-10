import json
import os


def get_json_path(name: str) -> str:
    return os.path.abspath(__file__).replace("utils.py", "") + f"../../json/{name}.json"


def read_json_file(name: str) -> dict | list:
    return json.loads(open(get_json_path(name), "r").read())


def save_json_file(name: str, data: dict | list) -> None:
    name += ".json"

    with open(name, "w") as f:
        json.dump(data, f, indent=4)
