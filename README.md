# Format Fusion 

This is the tool's CLI for converting various formats.

## Using

Format Fusion supports two commands for conversion:


| Name            | Commands              |
|-----------------|-----------------------|
| JSON to YAML    | `format-fusion yaml`  |
| Image to Base64 | `format-fusion image` |

### Usage example
Command to generate from JSON to YAML:

```shell
format-fusion yaml D:\response_api.json
```

Or you can perform the conversion in reverse order: **from YAML to JSON**

```shell
format-fusion yaml D:\response_api.yaml --reverse
```

The result of executing the command will be the creation of a YAML file named `output.yaml` or a JSON file named `output.json`

Optionally, you can specify where to save the converted files:

``
format-fusion yaml D:\screenshot.png --output D:\data.txt
``

This option is available for all commands.
## Install 

``
pip install cli-format-fusion
``

## Resources

- [Issue Tracker](https://github.com/Nottezz/format-fusion-cli/issues)