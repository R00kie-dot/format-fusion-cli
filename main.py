"""
Usage:
  main.py run <input_file> [--output=<output_file>]

Options:
  -h --help                Show helps.
  --output=<output_file>   Output YAML file [default: output.yaml].
"""

import json
import yaml
from docopt import docopt


def convert_json_to_yaml(input_file):
    with open(input_file, "r", encoding='utf-8') as file:
        json_dict = json.load(file)
    yaml_string = yaml.dump(json_dict)
    return yaml_string


def main():
    arguments = docopt(__doc__)
    input_file = arguments['<input_file>']
    output_file = arguments['--output']

    yaml_string = convert_json_to_yaml(input_file)

    with open(output_file, "w", encoding='utf-8') as file:
        file.write(yaml_string)
    print(f"Converted JSON from {input_file} to YAML and saved to {output_file}")


if __name__ == "__main__":
    main()
