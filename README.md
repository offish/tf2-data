# tf2-data
[![License](https://img.shields.io/github/license/offish/tf2-data.svg)](https://github.com/offish/tf2-data/blob/master/LICENSE)
[![Stars](https://img.shields.io/github/stars/offish/tf2-data.svg)](https://github.com/offish/tf2-data/stargazers)
[![Issues](https://img.shields.io/github/issues/offish/tf2-data.svg)](https://github.com/offish/tf2-data/issues)
[![Size](https://img.shields.io/github/repo-size/offish/tf2-data.svg)](https://github.com/offish/tf2-data)
[![Discord](https://img.shields.io/discord/467040686982692865?color=7289da&label=Discord&logo=discord)](https://discord.gg/t8nHSvA)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

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
python -m unittest
```

## Update files after new update
To update the local files after a TF2 update run this snippet.

```python
from tf2_data.schema import Schema, SchemaItems, IEconItems

api_key = "STEAM_API_KEY"
schema = Schema(api_key=api_key)
schema.set_effects()

ieconitems = IEconItems(api_key)
items = ieconitems.set_all_schema_items()

schema_items = SchemaItems(items)
schema_items.map_defindex_name()
schema_items.map_defindex_full_name()
```
