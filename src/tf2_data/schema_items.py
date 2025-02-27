from .constants import DEFINDEX_FULL_NAMES_PATH, DEFINDEX_NAMES_PATH, SCHEMA_ITEMS_PATH
from .utils import read_json_file, write_json_file


class SchemaItems:
    def __init__(
        self,
        schema_items: str | list[dict] = "",
        defindex_names: str | dict = "",
        defindex_full_names: str | dict = "",
    ) -> None:
        if not schema_items:
            schema_items = read_json_file(SCHEMA_ITEMS_PATH)

        if not defindex_names:
            defindex_names = read_json_file(DEFINDEX_NAMES_PATH)

        if not defindex_full_names:
            defindex_full_names = read_json_file(DEFINDEX_FULL_NAMES_PATH)

        if isinstance(schema_items, str):
            schema_items = read_json_file(schema_items)

        if isinstance(defindex_names, str):
            defindex_names = read_json_file(defindex_names)

        if isinstance(defindex_full_names, str):
            defindex_full_names = read_json_file(defindex_full_names)

        self.schema_items = schema_items
        self.defindex_names = defindex_names
        self.defindex_full_names = defindex_full_names

    def map_defindex_name(self) -> dict:
        data = {}

        for item in self.schema_items:
            name = item["item_name"]
            defindex = item["defindex"]

            # map both ways for ease of use
            # defindex as key is str
            data[str(defindex)] = name

            # map name to all defindexes
            # e.g. mann co key has multiple defindexes
            if name not in data:
                # defindex as value are ints
                data[name] = [defindex]
            else:
                data[name] += [defindex]

        self.defindex_names = data

        write_json_file(DEFINDEX_NAMES_PATH, data)

        return data

    def map_defindex_full_name(self) -> dict:
        data = {}

        for item in self.schema_items:
            name = item["name"]
            defindex = item["defindex"]

            # map both ways for ease of use
            # defindex as key is str
            data[str(defindex)] = name

            # map name to all defindexes
            # e.g. mann co key has multiple defindexes
            if name not in data:
                # defindex as value are ints
                data[name] = [defindex]
            else:
                data[name] += [defindex]

        self.defindex_full_names = data

        write_json_file(DEFINDEX_FULL_NAMES_PATH, data)

        return data
