from os import getenv

from dotenv import load_dotenv

from src.tf2_data import IEconItems, Schema, SchemaItems

assert load_dotenv()

api_key = getenv("STEAM_API_KEY")


if __name__ == "__main__":
    schema = Schema(api_key=api_key)
    schema.set_effects()

    ieconitems = IEconItems(api_key)
    items = ieconitems.set_all_schema_items()

    schema_items = SchemaItems(items)
    schema_items.map_defindex_name()
    schema_items.map_defindex_full_name()
