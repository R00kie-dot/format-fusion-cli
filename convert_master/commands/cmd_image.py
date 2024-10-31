"""
Run converting JSON to YAML

Usage:
    main.py [g-opts] image <path>

Arguments:
    <path>                      Path to image
"""
import logging
import os
from converting import Converting
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

def run_convert(opts):
    image_file = get_image_path(opts)
    convert = Converting(input_file=image_file)
    base64_image = convert.convert_image_to_base64()
    return logger.info(base64_image)
