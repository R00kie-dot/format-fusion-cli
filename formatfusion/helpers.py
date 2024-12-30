import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)

VALID_EXTENSIONS = {"json", "yaml", "png", "jpg"}


def get_file_extension(filename: Path) -> str:
    if not filename.name:
        raise ValueError("Filename cannot be empty.")
    return filename.suffix.lstrip(".")


def validate_files(input_file: Path, output_file: Path) -> bool:
    if not os.path.isfile(input_file):
        logger.error(f"The file '{input_file}' does not exist")
        return False

    input_extension = get_file_extension(input_file)
    if input_extension not in VALID_EXTENSIONS:
        logger.error(
            f"Invalid format '{input_extension}'. Acceptable formats: {', '.join(VALID_EXTENSIONS)}"
        )
        return False

    if input_extension == "json" and get_file_extension(output_file) != "yaml":
        logger.error(
            "For a JSON input file, the output file must have the extension '.yaml'."
        )
        return False

    if input_extension == "yaml" and get_file_extension(output_file) != "json":
        logger.error(
            "For a YAML input file, the output file must have the extension '.json'."
        )
        return False
    return True
