from .utils import read_lib_json_file

__all__ = [
    "EFFECTS",
    "SCHEMA_ITEMS",
    "ITEM_NAME_IDS",
    "DEFINDEX_NAMES",
    "DEFINDEX_FULL_NAMES",
]

EFFECTS = read_lib_json_file("effects")
SCHEMA_ITEMS = read_lib_json_file("schema_items")
ITEM_NAME_IDS = read_lib_json_file("item_nameids")
DEFINDEX_NAMES = read_lib_json_file("defindex_names")
DEFINDEX_FULL_NAMES = read_lib_json_file("defindex_full_names")
