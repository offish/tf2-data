import time
from typing import Any

import requests

from .paths import SCHEMA_ITEMS_PATH, SCHEMA_OVERVIEW_PATH
from .utils import write_json_file


class Endpoint:
    SCHEMA_OVERVIEW = "GetSchemaOverview/v0001"
    PLAYER_ITEMS = "GetPlayerItems/v0001"
    SCHEMA_ITEMS = "GetSchemaItems/v1"
    STORE_DATA = "GetStoreMetaData/v1"
    SCHEMA_URL = "GetSchemaURL/v1"


class IEconItems:
    def __init__(self, api_key: str) -> None:
        self.__api_key = api_key

    def _get_request(self, endpoint: str, params: dict | None = None) -> Any:
        url = "https://api.steampowered.com/IEconItems_440/" + endpoint

        if params is None:
            params = {}

        params["key"] = self.__api_key

        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_player_items(self, steamid: str) -> dict:
        return self._get_request(Endpoint.PLAYER_ITEMS, {"steamid": steamid})

    def get_schema_items(self, start: int = 0, language: str = "en") -> dict:
        return self._get_request(
            Endpoint.SCHEMA_ITEMS, {"language": language.lower(), "start": start}
        )

    def get_all_schema_items(self, language: str = "en", sleep: float = 5.0) -> list:
        items = []
        start = 0

        while start is not None:
            response = self.get_schema_items(start, language=language)["result"]
            items += response.get("items", [])
            start = response.get("next")
            time.sleep(sleep)

        return items

    def get_schema_overview(self, language: str = "en") -> dict:
        return self._get_request(
            Endpoint.SCHEMA_OVERVIEW, {"language": language.lower()}
        )

    def get_schema_url(self) -> dict:
        return self._get_request(Endpoint.SCHEMA_URL, {})

    def get_store_meta_data(self, language: str = "en") -> dict:
        return self._get_request(Endpoint.STORE_DATA, {"language": language.lower()})

    def set_schema_overview(self, language: str = "en") -> dict:
        schema = self.get_schema_overview(language)
        write_json_file(SCHEMA_OVERVIEW_PATH, schema)
        return schema

    def set_all_schema_items(self, language: str = "en", sleep: float = 5.0) -> list:
        items = self.get_all_schema_items(language, sleep)
        write_json_file(SCHEMA_ITEMS_PATH, items)
        return items
