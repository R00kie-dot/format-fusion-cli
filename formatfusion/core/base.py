import typing as t
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class Base:
    def __init__(self, input_file: Path, output_file: Path | None = None):
        self.input_file = input_file
        self.output_file = output_file

    def save_result(self, result: str, success_message: str) -> None:
        if not self.output_file:
            raise ValueError("Output file is not specified.")

        with open(self.output_file, "w", encoding="utf-8") as file:
            file.write(result)

        logger.info(success_message)
