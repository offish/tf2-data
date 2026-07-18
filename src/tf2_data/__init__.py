# flake8: noqa
__title__ = "tf2-data"
__author__ = "offish"
__version__ = "1.1.0"
__license__ = "MIT"

from .data import (
    COLORS,
    EXTERIORS,
    KILLSTREAKS,
    QUALITIES,
    QUALITY_COLORS,
    WEARS,
    SHEENS,
    SPELLS,
    PARTS,
    PAINTS,
    KILLSTREAKERS,
    EYES,
    STRANGE_PARTS,
    HALLOWEEN_SPELLS,
    KILLSTREAK_TIERS,
)
from .files import (
    EFFECTS,
    SCHEMA_ITEMS,
    ITEM_NAME_IDS,
    DEFINDEX_FULL_NAMES,
    DEFINDEX_NAMES,
    CRATE_SERIES,
    WAR_PAINTS,
)
from .iecon_items import IEconItems
from .schema import Schema
from .schema_items import SchemaItems
