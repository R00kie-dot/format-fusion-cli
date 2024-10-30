import os
import logging

logger = logging.getLogger(__name__)

VALID_EXTENSIONS = {"json", "png", "jpg"}

def get_file_extension(filename: str):
    return os.path.splitext(filename)[-1].lstrip('.')


def validate_files(input_file, output_file) -> bool:
    if not os.path.isfile(input_file):
        logger.error(f"The file '{input_file}' does not exist")
        return False

    input_extension = get_file_extension(input_file)
    if input_extension not in VALID_EXTENSIONS:
        logger.error(
            f"Invalid format '{input_extension}'. Acceptable formats: {', '.join(VALID_EXTENSIONS)}")
        return False

    if input_extension == "json" and get_file_extension(output_file) != "yaml":
        logger.error("For a JSON input file, the output file must have the extension '.yaml'.")
        return False

    return True
