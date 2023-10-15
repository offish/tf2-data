from src.tf2_data import KILLSTREAKS, QUALITIES, EFFECTS, COLORS, WEARS
from src.tf2_data.utils import read_lib_json_file

from unittest import TestCase


class TestStatic(TestCase):
    def test_up_to_date(self):
        killstreaks = read_lib_json_file("killstreaks")
        qualties = read_lib_json_file("qualities")
        effects = read_lib_json_file("effects")
        colors = read_lib_json_file("colors")
        wears = read_lib_json_file("wears")

        self.assertEqual(killstreaks, KILLSTREAKS)
        self.assertEqual(qualties, QUALITIES)
        self.assertEqual(effects, EFFECTS)
        self.assertEqual(colors, COLORS)
        self.assertEqual(wears, WEARS)
