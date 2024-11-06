import base64
import json
import logging

import yaml

logger = logging.getLogger(__name__)


class Converting:
    def __init__(self, input_file: str, output_file: str | None = None):
        self.input_file = input_file
        self.output_file = output_file

    def convert_json_to_yaml(self) -> str:
        with open(self.input_file, "r", encoding="utf-8") as file:
            json_dict = json.load(file)
        return yaml.dump(json_dict, sort_keys=False)

    def convert_image_to_base64(self) -> str:
        with open(self.input_file, "rb") as image:
            return base64.b64encode(image.read()).decode("utf-8")
