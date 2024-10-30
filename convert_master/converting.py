import base64
import json
import logging
import os

import yaml

logger = logging.getLogger(__name__)


class Converting:

    def __init__(self, input_file: str, output_file: str | None = None):
        self.input_file = input_file
        self.output_file = output_file

    def convert_json_to_yaml(self) -> None:
        with open(self.input_file, "r", encoding='utf-8') as file:
            json_dict = json.load(file)
        yaml_string = yaml.dump(json_dict, sort_keys=False)

        with open(self.output_file, "w", encoding='utf-8') as file:
            file.write(yaml_string)
        logger.info(f"The JSON from {self.input_file} was converted to YAML and saved in {self.output_file}")

    def convert_image_to_base64(self) -> str:
        with open(self.input_file, "rb") as image:
            base64_string = base64.b64encode(image.read()).decode("utf-8")

        return base64_string