import base64
import json
import logging
import os

import yaml

logger = logging.getLogger(__name__)


class Converting:
    VALID_EXTENSIONS = {"json", "png", "jpg"}

    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file

    def run(self):
        if not self.validate_files():
            return
        else:
            if self.get_file_extension(self.input_file) == "json":
                return self.convert_json_to_yaml()
            elif self.get_file_extension(self.input_file) == "png" or (
                    self.get_file_extension(self.input_file) == "jpg"):
                return self.convert_image_to_base64()

    def convert_json_to_yaml(self) -> None:
        with open(self.input_file, "r", encoding='utf-8') as file:
            json_dict = json.load(file)
        yaml_string = yaml.dump(json_dict, sort_keys=False)

        with open(self.output_file, "w", encoding='utf-8') as file:
            file.write(yaml_string)
        logger.info(f"The JSON from {self.input_file} was converted to YAML and saved in {self.output_file}")

    def convert_image_to_base64(self) -> None:
        with open(self.input_file, "rb") as image:
            base64_string = base64.b64encode(image.read()).decode("utf-8")

        image_name = os.path.basename(self.input_file)

        with open(self.output_file, "w", encoding='utf-8') as file:
            file.write(base64_string)
        logger.info(F"The {image_name} has been converted and saved at {self.output_file}")

    @staticmethod
    def get_file_extension(filename: str):
        return os.path.splitext(filename)[-1].lstrip('.')

    def validate_files(self) -> bool:
        if not os.path.isfile(self.input_file):
            logger.error(f"The file '{self.input_file}' does not exist")
            return False

        input_extension = self.get_file_extension(self.input_file)
        if input_extension not in self.VALID_EXTENSIONS:
            logger.error(
                f"Invalid format '{input_extension}'. Acceptable formats: {', '.join(self.VALID_EXTENSIONS)}")
            return False

        if input_extension == "json" and self.get_file_extension(self.output_file) != "yaml":
            logger.error("For a JSON input file, the output file must have the extension '.yaml'.")
            return False

        return True
