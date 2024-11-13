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
import os

from formatfusion.converter import Converter

logger = logging.getLogger(__name__)


def run(opts):
    logger.info("Start converting..")
    return run_convert(opts)


def get_image_path(opts):
    opt_image_path = opts["<path>"]
    image_path = os.path.abspath(opt_image_path)
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"File not found: {image_path}.")
    return image_path


def get_output_path(opts):
    opt_file_path = opts["--output"] if opts["--output"] is not None else "output.txt"
    file_path = os.path.abspath(opt_file_path)
    return file_path


def run_convert(opts):
    image_file = get_image_path(opts)
    output_path = get_output_path(opts)

    convert = Converter(input_file=image_file)
    base64_image = convert.convert_image_to_base64()

    with open(output_path, "w") as file:
        file.write(base64_image)
        logger.info(f"The converted image was saved in {output_path}")
