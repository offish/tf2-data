from .constants import EFFECTS_PATH, QUALITIES_PATH, SCHEMA_OVERVIEW_PATH
from .iecon_items import IEconItems
from .utils import read_json_file, write_json_file


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
