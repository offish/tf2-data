from .utils import get_json_path, read_json_file, write_json_file, read_lib_json_file

from tf2_utils import IEconItems


SCHEMA_OVERVIEW_PATH = get_json_path("schema_overview")
SCHEMA_ITEMS_PATH = get_json_path("schema_items")
QUALITIES_PATH = get_json_path("qualities")
EFFECTS_PATH = get_json_path("effects")

EFFECTS = read_json_file(EFFECTS_PATH)


class SchemaItems:
    def __init__(
        self, schema_items: str | list[dict] = "", defindex_names: str | dict = ""
    ) -> None:
        if not schema_items:
            schema_items = read_lib_json_file("schema_items")

        if not defindex_names:
            defindex_names = read_lib_json_file("defindex_names")

        if isinstance(schema_items, str):
            schema_items = read_json_file(schema_items)

        if isinstance(defindex_names, str):
            defindex_names = read_json_file(defindex_names)

        self.schema_items = schema_items
        self.defindex_names = defindex_names

    def map_defindex_name(self) -> dict:
        data = {}

        for item in self.schema_items:
            name = item["item_name"]
            defindex = item["defindex"]

            data[defindex] = name
            data[name] = defindex

        self.defindex_names = data

        return data


class Schema:
    def __init__(
        self, schema: dict | str = {}, api_key: str = "", language: str = "en"
    ) -> None:
        if api_key:
            schema = IEconItems(api_key).get_schema_overview(language)

        if not schema:
            schema = SCHEMA_OVERVIEW_PATH

        if isinstance(schema, str):
            schema = read_json_file(schema)

        self.schema = schema

    def set_effects(self) -> dict:
        path = get_json_path("effects")
        effects = self.schema["result"]["attribute_controlled_attached_particles"]

        data = {}

        for effect in effects:
            effect_name = effect["name"]
            effect_id = effect["id"]

            # map both ways for ease of use
            data[effect_name] = effect_id
            data[effect_id] = effect_name

        write_json_file(path, data)
        return data

    def set_qualities(self) -> dict:
        path = get_json_path("qualities")
        qualtiy_ids = self.schema["result"]["qualities"]
        qualtiy_names = self.schema["result"]["qualityNames"]

        data = {}

        for q in qualtiy_ids:
            quality_name = qualtiy_names[q]
            quality_id = qualtiy_ids[q]

            # map both ways for ease of use
            data[quality_name] = quality_id
            data[quality_id] = quality_name

        write_json_file(path, data)
        return data


class IEconItems(IEconItems):
    def __init__(self, api_key: str) -> None:
        super().__init__(api_key)

    def set_schema_overview(self, language: str = "en") -> dict:
        schema = self.get_schema_overview(language)
        write_json_file(SCHEMA_OVERVIEW_PATH, schema)
        return schema

    def set_all_schema_items(self, language: str = "en", sleep: float = 5.0) -> list:
        items = self.get_all_schema_items(language, sleep)
        write_json_file(SCHEMA_ITEMS_PATH, items)
        return items
