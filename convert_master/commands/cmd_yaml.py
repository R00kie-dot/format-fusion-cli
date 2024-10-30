"""
Run converting JSON to YAML

Usage:
    main.py [g-opts] yaml <path> [options]

Arguments:
    <path>                      Path to JSON file

Options:
    --output <output_path>      Path to save YAML file [default: output.yaml]
"""
import logging
from converting import Converting
from helpers import validate_files
import os

logger = logging.getLogger(__name__)


def run(opts):
    logger.info("Start converting..")
    return run_convert(opts)


def get_json_path(opts):
    opt_json_path = opts["<path>"]
    json_path = os.path.abspath(opt_json_path)
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"File not found: {json_path}.")
    return json_path


def get_output_path(opts):
    opt_yaml_path = opts["--output"] if opts["--output"] is not None else "output.yaml"
    yaml_path = os.path.abspath(opt_yaml_path)
    return yaml_path


def run_convert(opts) -> None:
    json_file = get_json_path(opts)
    yaml_file = get_output_path(opts)
    if not validate_files(json_file, yaml_file):
        return

    convert = Converting(input_file=json_file, output_file=yaml_file)
    yaml_string = convert.convert_json_to_yaml()

    with open(yaml_file, "w", encoding='utf-8') as file:
        file.write(yaml_string)
    logger.info(f"The JSON from {json_file} was converted to YAML and saved in {yaml_file}")


