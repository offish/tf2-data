from .utils import read_json_file

from tf2_sku import to_sku


class Data:
    def __init__(self) -> None:
        self.schema_items: list[dict] = read_json_file("schema_items")
        self.defindex_names: dict = read_json_file("defindex_names")

    def map_defindex_name(self) -> dict:
        data = {}

        for item in self.schema_items:
            name = item["item_name"]
            defindex = item["defindex"]

            data[defindex] = name
            data[name] = defindex

        # self.defindex_names = data

        return data

    def defindex_to_image_url(self, defindex: int, large: bool = False) -> str:
        # random craft hat image => ellis' cap
        if isinstance(defindex, str):
            defindex = int(defindex)

        if defindex == -100:
            defindex = 263

        for item in self.schema_items:
            if item["defindex"] != defindex:
                continue

            return item["image_url"] if not large else item["image_url_large"]

        return ""

    def sku_to_image_url(self, sku: str, large: bool = False) -> str:
        defindex = sku.split(";")[:-1][0]
        return self.defindex_to_image_url(defindex, large)

    def name_to_sku(self, name: str) -> str:
        """This is not accurate, be careful when using this."""
        parts = name.split(" ")

        defindex = -1
        craftable = True
        quality = 6

        for part in parts:
            if part in ["Uncraftable", "Non-Craftable"]:
                craftable = False

            match part:
                case "Genuine":
                    quality = 1

                case "Vintage":
                    quality = 3

                case "Strange":
                    quality = 11

        defindex_name = name

        while True:
            defindex = self.defindex_names.get(defindex_name, -1)

            if defindex != -1:
                break

            try:
                index = defindex_name.index(" ")
            except ValueError:
                break

            defindex_name = defindex_name[index + 1 :]

        sku_properties = {
            "defindex": defindex,
            "quality": quality,
            "craftable": craftable,
        }

        return to_sku(sku_properties)
