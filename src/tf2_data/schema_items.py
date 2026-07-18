from .paths import CRATE_SERIES_PATH, DEFINDEX_FULL_NAMES_PATH, DEFINDEX_NAMES_PATH
from .utils import read_json_file, read_lib_json_file, write_json_file


class SchemaItems:
    def __init__(
        self,
        schema_items: str | list[dict] | None = None,
        defindex_names: str | dict | None = None,
        defindex_full_names: str | dict | None = None,
    ) -> None:
        if not schema_items:
            schema_items = read_lib_json_file("schema_items")

        if not defindex_names:
            defindex_names = read_lib_json_file("defindex_names")

        if not defindex_full_names:
            defindex_full_names = read_lib_json_file("defindex_full_names")

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

    @staticmethod
    def _is_crate_name(name: str) -> bool:
        if name.endswith(" War Paint Case") or name.endswith(" Cosmetic Case"):
            return True

        if (
            name.endswith(" Case")
            and "\n" not in name
            and name not in ["Cold Case", "Hot Case"]
        ):
            return True

        return False

    def update_crate_series(self) -> None:
        data = read_json_file(CRATE_SERIES_PATH)

        for name in self.defindex_names:
            if self._is_crate_name(name) and name not in data:
                defindex = self.defindex_names[name][0]
                data[name] = defindex

        write_json_file(CRATE_SERIES_PATH, data)
