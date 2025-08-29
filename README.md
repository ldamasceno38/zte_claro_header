# ZTE Claro Header Editor

Modifies specific bytes in Claro ZTE modem binary file headers.
Fixes error when you import a .bin file and NO CHANGES are made.

Tested on
- CLARO ZXHN ZTE F6600P
- CLARO ZXHN ZTE F6645P

## Usage

```bash
python zte_claro_header.py --bin <FILE>
```
**Note**: Creates automatic `.backup` file before modification.
