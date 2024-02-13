from .utils import get_json_path, read_json_file, write_json_file

import time

import requests


DEFINDEX_FULL_NAMES_PATH = get_json_path("defindex_full_names")
SCHEMA_OVERVIEW_PATH = get_json_path("schema_overview")
DEFINDEX_NAMES_PATH = get_json_path("defindex_names")
SCHEMA_ITEMS_PATH = get_json_path("schema_items")
QUALITIES_PATH = get_json_path("qualities")
EFFECTS_PATH = get_json_path("effects")


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
        effects = self.schema["result"]["attribute_controlled_attached_particles"]

        data = {}

        for effect in effects:
            effect_name = effect["name"]
            effect_id = effect["id"]

            # map both ways for ease of use
            data[effect_name] = effect_id
            data[effect_id] = effect_name

        write_json_file(EFFECTS_PATH, data)
        return data

    def set_qualities(self) -> dict:
        qualtiy_ids = self.schema["result"]["qualities"]
        qualtiy_names = self.schema["result"]["qualityNames"]

        data = {}

        for q in qualtiy_ids:
            quality_name = qualtiy_names[q]
            quality_id = qualtiy_ids[q]

            # map both ways for ease of use
            data[quality_name] = quality_id
            data[quality_id] = quality_name

        write_json_file(QUALITIES_PATH, data)
        return data


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


class IEconItems:
    API_URL = "https://api.steampowered.com/IEconItems_440"
    SCHEMA_OVERVIEW = API_URL + "/GetSchemaOverview/v0001"
    PLAYER_ITEMS = API_URL + "/GetPlayerItems/v0001"
    SCHEMA_ITEMS = API_URL + "/GetSchemaItems/v1"
    STORE_DATA = API_URL + "/GetStoreMetaData/v1"
    SCHEMA_URL = API_URL + "/GetSchemaURL/v1"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def __get(self, url: str, params: dict = {}) -> dict:
        params["key"] = self.api_key

        res = requests.get(url, params=params)

        try:
            return res.json()
        except Exception:
            return {}

    def get_player_items(self, steamid: str) -> dict:
        return self.__get(self.PLAYER_ITEMS, {"steamid": steamid})

    def get_schema_items(self, start: int = 0, language: str = "en") -> dict:
        return self.__get(
            self.SCHEMA_ITEMS, {"language": language.lower(), "start": start}
        )

    def get_all_schema_items(self, language: str = "en", sleep: float = 5.0) -> list:
        items = []
        start = 0

        while start is not None:
            response = self.get_schema_items(start, language=language)["result"]
            items += response.get("items", [])
            start = response.get("next")  # None if not found
            time.sleep(sleep)

        return items

    def get_schema_overview(self, language: str = "en") -> dict:
        return self.__get(self.SCHEMA_OVERVIEW, {"language": language.lower()})

    def get_schema_url(self) -> dict:
        return self.__get(self.SCHEMA_URL, {})

    def get_store_meta_data(self, language: str = "en") -> dict:
        return self.__get(self.STORE_DATA, {"language": language.lower()})

    def set_schema_overview(self, language: str = "en") -> dict:
        schema = self.get_schema_overview(language)
        write_json_file(SCHEMA_OVERVIEW_PATH, schema)
        return schema

    def set_all_schema_items(self, language: str = "en", sleep: float = 5.0) -> list:
        items = self.get_all_schema_items(language, sleep)
        write_json_file(SCHEMA_ITEMS_PATH, items)
        return items
