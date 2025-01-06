import json
from pathlib import Path

import yaml

from formatfusion.models.file_converter_model import FileConverterModel
from .base import Base


class ConverterYAMLandJSON(Base):
    def __init__(self, input_file: Path, output_file: Path):
        super().__init__(input_file, output_file)
        validated_data = FileConverterModel(
            input_file=Path(input_file),
            output_file=Path(output_file) if output_file else None,
        )
        self.input_file = validated_data.input_file
        self.output_file = validated_data.output_file

    def convert_json_to_yaml(self) -> None:
        with open(self.input_file, "r", encoding="utf-8") as file:
            json_dict = json.load(file)
        result = yaml.dump(json_dict, sort_keys=False)
        self.save_result(
            result,
            f"The JSON from {self.input_file} was converted to YAML and saved in {self.output_file.as_uri()}",
        )

    def convert_yaml_to_json(self) -> None:
        with open(self.input_file, "r", encoding="utf-8") as file:
            yaml_dict = yaml.safe_load(file)
        result = json.dumps(yaml_dict, indent=4, ensure_ascii=False)
        self.save_result(
            result,
            f"The YAML from {self.input_file} was converted to JSON and saved in {self.output_file.as_uri()}",
        )
