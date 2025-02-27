from src.tf2_data import COLORS, EFFECTS, KILLSTREAKS, QUALITIES, WEARS
from src.tf2_data.utils import read_lib_json_file


def test_up_to_date() -> None:
    killstreaks = read_lib_json_file("killstreaks")
    qualties = read_lib_json_file("qualities")
    effects = read_lib_json_file("effects")
    colors = read_lib_json_file("colors")
    wears = read_lib_json_file("wears")

    assert killstreaks == KILLSTREAKS
    assert qualties == QUALITIES
    assert effects == EFFECTS
    assert colors == COLORS
    assert wears == WEARS
