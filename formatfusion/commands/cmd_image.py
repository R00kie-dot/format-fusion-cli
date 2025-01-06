"""
Run converting JSON to YAML

Usage:
    format-fusion [g-opts] image <path> [options]

Arguments:
    <path>                      Path to image

Options:
    --output <output_path>      Path to save file [default: output.txt]
"""
import logging
import typing as t
from pathlib import Path

from formatfusion.core.image import ConverterImage

logger = logging.getLogger(__name__)


def run(opts: t.Dict[str, t.Any]) -> t.Any:
    logger.info("Start converting..")
    return run_convert(opts)


def get_image_path(opts: t.Dict[str, t.Any]) -> Path:
    opt_image_path = opts["<path>"]
    image_path = Path(opt_image_path).resolve()
    if not image_path.exists():
        raise FileNotFoundError(f"File not found: {image_path}.")
    return image_path


def get_output_path(opts: t.Dict[str, t.Any]) -> Path:
    opt_file_path = opts["--output"] if opts["--output"] is not None else "output.txt"
    file_path = Path(opt_file_path).resolve()
    return file_path


def run_convert(opts: t.Dict[str, t.Any]) -> None:
    image_file = get_image_path(opts)
    output_path = get_output_path(opts)

    try:
        convert = ConverterImage(input_file=image_file, output_file=output_path)
        convert.convert_image_to_base64()
    except ValueError as e:
        logger.error(f"Validation error: {e}")

