# Format Fusion 

This is the tool's CLI for converting various formats.

## Using

Format Fusion supports two commands for conversion:
- JSON to YAML - `format-fusion yaml`
- Image to Base64 - `format-fusion image`

### Usage example
Command to generate from JSON to YAML:

``
format-fusion yaml D:\response_api.json
``

The result of executing the command will be the generation of a YAML named `output.yaml`

Optionally, you can specify where to save the converted files:

``
format-fusion yaml D:\screenshot.png --output D:\data.txt
``

This option is available for all commands.
## Install 

``
pip install format-fusion-cli
``

## Resources

- [Issue Tracker](https://github.com/Nottezz/format-fusion-cli/issues)