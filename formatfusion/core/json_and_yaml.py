import json
import yaml

from .base import Base


class ConverterYAMLandJSON(Base):

    def convert_json_to_yaml(self) -> None:
        with open(self.input_file, "r", encoding="utf-8") as file:
            json_dict = json.load(file)
        result = yaml.dump(json_dict, sort_keys=False)
        self.save_result(
            result,
            f"The JSON from {self.input_file} was converted to YAML and saved in {self.output_file}"
        )

    def convert_yaml_to_json(self) -> None:
        with open(self.input_file, "r", encoding="utf-8") as file:
            yaml_dict = yaml.safe_load(file)
        result = json.dumps(yaml_dict, indent=4, ensure_ascii=False)
        self.save_result(
            result,
            f"The YAML from {self.input_file} was converted to JSON and saved in {self.output_file}"
        )
