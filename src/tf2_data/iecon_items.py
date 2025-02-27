import time

import requests

from .constants import SCHEMA_ITEMS_PATH, SCHEMA_OVERVIEW_PATH
from .utils import write_json_file


class IEconItems:
    API_URL = "https://api.steampowered.com/IEconItems_440"
    SCHEMA_OVERVIEW = API_URL + "/GetSchemaOverview/v0001"
    PLAYER_ITEMS = API_URL + "/GetPlayerItems/v0001"
    SCHEMA_ITEMS = API_URL + "/GetSchemaItems/v1"
    STORE_DATA = API_URL + "/GetStoreMetaData/v1"
    SCHEMA_URL = API_URL + "/GetSchemaURL/v1"

    def __init__(self, api_key: str) -> None:
        self.__api_key = api_key

    def _get(self, url: str, params: dict = {}) -> dict:
        params["key"] = self.__api_key

        res = requests.get(url, params=params)

        try:
            return res.json()
        except Exception:
            return {}

    def get_player_items(self, steamid: str) -> dict:
        return self._get(self.PLAYER_ITEMS, {"steamid": steamid})

    def get_schema_items(self, start: int = 0, language: str = "en") -> dict:
        return self._get(
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
        return self._get(self.SCHEMA_OVERVIEW, {"language": language.lower()})

    def get_schema_url(self) -> dict:
        return self._get(self.SCHEMA_URL, {})

    def get_store_meta_data(self, language: str = "en") -> dict:
        return self._get(self.STORE_DATA, {"language": language.lower()})

    def set_schema_overview(self, language: str = "en") -> dict:
        schema = self.get_schema_overview(language)
        write_json_file(SCHEMA_OVERVIEW_PATH, schema)
        return schema

    def set_all_schema_items(self, language: str = "en", sleep: float = 5.0) -> list:
        items = self.get_all_schema_items(language, sleep)
        write_json_file(SCHEMA_ITEMS_PATH, items)
        return items
