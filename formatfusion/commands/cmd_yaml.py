"""
Run converting JSON to YAML

Usage:
    format-fusion [g-opts] yaml <path> [options]

Arguments:
    <path>                      Path to JSON or YAML file

Options:
    --output <output_path>      Path to save YAML or JSON file
    --reverse                   A flag that allows you to convert from YAML to JSON
"""
import logging
import typing as t
from pathlib import Path

from formatfusion.core.json_and_yaml import ConverterYAMLandJSON

logger = logging.getLogger(__name__)


def run(opts: t.Dict[str, t.Any]) -> t.Any:
    logger.info("Start converting..")
    return run_convert(opts)


def get_input_file_path(opts: t.Dict[str, t.Any]) -> Path:
    opt_input_path = opts["<path>"]
    input_path = Path(opt_input_path).resolve()
    if not input_path.exists():
        raise FileNotFoundError(f"File not found: {input_path}.")
    return input_path


def get_output_file_path(opts: t.Dict[str, t.Any], input_file: Path) -> Path:
    if opts["--output"] is not None:
        output_path = Path(opts["--output"]).resolve()
    else:
        if input_file.suffix == ".json":
            default_output = input_file.parent / "output.yaml"
        elif input_file.suffix == ".yaml":
            default_output = input_file.parent / "output.json"
        else:
            raise ValueError(f"Unsupported input file extension: {input_file.suffix}.")
        output_path = default_output.resolve()

    return output_path


def run_convert(opts: t.Dict[str, t.Any]) -> None:
    input_file = get_input_file_path(opts)
    output_file = get_output_file_path(opts, input_file)
    try:
        convert = ConverterYAMLandJSON(input_file=input_file, output_file=output_file)
        if opts["--reverse"]:
            convert.convert_yaml_to_json()
        else:
            convert.convert_json_to_yaml()
    except ValueError as e:
        logger.error(f"Validation error: {e}")
