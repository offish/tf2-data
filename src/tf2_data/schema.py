from .iecon_items import IEconItems
from .paths import EFFECTS_PATH, SCHEMA_OVERVIEW_PATH
from .utils import read_json_file, write_json_file


class Schema:
    def __init__(
        self,
        schema: str | dict | None = None,
        api_key: str | None = None,
        language: str = "en",
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
