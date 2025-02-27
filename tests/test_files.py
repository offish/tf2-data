import pytest

from src.tf2_data import DEFINDEX_FULL_NAMES, DEFINDEX_NAMES


def test_defindex_names() -> None:
    assert DEFINDEX_NAMES["Team Captain"] == [378]
    assert DEFINDEX_NAMES["378"] == "Team Captain"

    with pytest.raises(KeyError):
        DEFINDEX_NAMES["The Team Captain"]


def test_defindex_full_names() -> None:
    assert DEFINDEX_FULL_NAMES["378"] == "The Team Captain"
    assert DEFINDEX_FULL_NAMES["The Team Captain"] == [378]

    with pytest.raises(KeyError):
        DEFINDEX_FULL_NAMES["Team Captain"]
