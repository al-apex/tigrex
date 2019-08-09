# tigrex

tigrex is a Python CLI Tool for searching and pricing Magic the Gathering cards using Scryfall's API.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install tigrex.

```bash
pip install tigrex
```

## Usage
All searches leverage a fuzzy search, meaning that the `[card_name]` does not have to be exact. Examples:
- `yuriko` will result in a search result of `Yuriko, the Tiger's Shadow`
- `watery` will result in a search result of `Watery Grave`

If a full name needs to be searched for, wrapping the `[card_name]` in `" "` can achieve this, `"[card_name]"`. Examples:
- `"yuriko, the tiger's shadow"` will result in a search result of `Yuriko, the Tiger's Shadow`
- `"watery grave"` will result in a search result of `Watery Grave`

Fuzzy search will fail if there are multiple results. Examples:`
- `path to` will fail and not bring up the card `Path to Exile``
- `"path to"` will fail and not bring up the card `Path to Exile`

## Commands
**search**
```bash
tigrex search [card-name]
```
![tigrex search](demo/tigrex-search.gif)

**price**
```
tigrex price [card-name]
```
![tigrex search](demo/tigrex-price.gif)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
