import unittest
from pathlib import Path
from unittest.mock import mock_open, patch

from formatfusion.core.json_and_yaml import ConverterYAMLandJSON


class TestConvertJsonToYaml(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
    @patch("formatfusion.core.base.Base.save_result")
    def test_convert_json_to_yaml(self, mock_save_result, mock_open):
        input_file = Path("/path/to/input/file.json")
        output_file = Path("/path/to/output/file.yaml")
        converter = ConverterYAMLandJSON(input_file=input_file, output_file=output_file)

        converter.convert_json_to_yaml()

        mock_open.assert_called_once_with(input_file, "r", encoding="utf-8")

        mock_save_result.assert_called_once_with(
            "key: value\n",
            f"The JSON from {input_file} was converted to YAML and saved in {output_file}",
        )

    @patch("builtins.open", new_callable=mock_open, read_data="key: value\n")
    @patch("formatfusion.core.base.Base.save_result")
    def test_convert_yaml_to_json(self, mock_save_result, mock_open):
        input_file = Path("/path/to/input/file.yaml")
        output_file = Path("/path/to/output/file.json")
        converter = ConverterYAMLandJSON(input_file=input_file, output_file=output_file)

        converter.convert_yaml_to_json()

        mock_open.assert_called_once_with(input_file, "r", encoding="utf-8")

        mock_save_result.assert_called_once_with(
            '{\n    "key": "value"\n}',
            f"The YAML from {input_file} was converted to JSON and saved in {output_file}",
        )
