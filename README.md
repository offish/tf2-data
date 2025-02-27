# tf2-data
[![Stars](https://img.shields.io/github/stars/offish/tf2-data.svg)](https://github.com/offish/tf2-data/stargazers)
[![Issues](https://img.shields.io/github/issues/offish/tf2-data.svg)](https://github.com/offish/tf2-data/issues)
[![Size](https://img.shields.io/github/repo-size/offish/tf2-data.svg)](https://github.com/offish/tf2-data)
[![Discord](https://img.shields.io/discord/467040686982692865?color=7289da&label=Discord&logo=discord)](https://discord.gg/t8nHSvA)
[![Downloads](https://img.shields.io/pypi/dm/tf2-data)](https://pypi.org/project/tf2-data/)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


Item schemas, unusual effects, SKUs and more which can be useful for TF2 trading. Implemented by [tf2-utils](https://github.com/offish/tf2-utils).

## Donate
- BTC: `bc1qntlxs7v76j0zpgkwm62f6z0spsvyezhcmsp0z2`
- [Steam Trade Offer](https://steamcommunity.com/tradeoffer/new/?partner=293059984&token=0-l_idZR)

## Setup
### Install
```bash
pip install tf2-data
# or 
python -m pip install tf2-data
```

### Updating
```bash
pip install --upgrade tf2-data
# or 
python -m pip install --upgrade tf2-data
```

## Testing
```bash
# tf2-data/
pytest
```

## Update files after new update
If the package is not up-to-date, run this snippet to update your local files.

```python
from tf2_data import Schema, SchemaItems, IEconItems

api_key = "STEAM_API_KEY"
schema = Schema(api_key=api_key)
schema.set_effects()

ieconitems = IEconItems(api_key)
items = ieconitems.set_all_schema_items()

schema_items = SchemaItems(items)
schema_items.map_defindex_name()
schema_items.map_defindex_full_name()
```
