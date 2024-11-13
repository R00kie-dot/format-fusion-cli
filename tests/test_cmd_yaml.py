import os
import tempfile
import unittest
from unittest.mock import patch

from formatfusion.commands.cmd_yaml import get_json_path, get_output_path, run_convert


class TestFormatFusionYaml(unittest.TestCase):
    def test_run_convert(self):
        with tempfile.NamedTemporaryFile(
            suffix=".json", delete=False
        ) as temp_json, tempfile.NamedTemporaryFile(
            suffix=".yaml", delete=False
        ) as temp_yaml:
            json_content = '{"key": "value"}'
            temp_json.write(json_content.encode())
            temp_json_path = temp_json.name
            temp_yaml_path = temp_yaml.name

        opts = {"<path>": temp_json_path, "--output": temp_yaml_path}

        run_convert(opts)

        with open(temp_yaml_path, "r", encoding="utf-8") as file:
            yaml_content = file.read()
            self.assertEqual(yaml_content, "key: value\n")

        os.remove(temp_json_path)
        os.remove(temp_yaml_path)

    def test_get_json_path_valid(self):
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as temp_json:
            temp_json_path = temp_json.name
        opts = {"<path>": temp_json_path}
        result = get_json_path(opts)
        self.assertEqual(result, os.path.abspath(temp_json_path))
        os.remove(temp_json_path)

    def test_get_json_path_invalid(self):
        opts = {"<path>": "nonexistent.json"}
        with self.assertRaises(FileNotFoundError):
            get_json_path(opts)

    def test_get_output_path(self):
        opts = {"--output": "custom_output.yaml"}
        result = get_output_path(opts)
        self.assertEqual(result, os.path.abspath("custom_output.yaml"))

        opts = {"--output": None}
        result = get_output_path(opts)
        self.assertEqual(result, os.path.abspath("output.yaml"))

    @patch(
        "formatfusion.commands.cmd_yaml.get_json_path",
        side_effect=FileNotFoundError("File not found: fake.json"),
    )
    @patch("formatfusion.commands.cmd_yaml.get_output_path", return_value="fake.yaml")
    def test_run_convert_file_not_found(self, mock_output, mock_json):
        opts = {"<path>": "fake.json", "--output": "fake.yaml"}

        with self.assertRaises(FileNotFoundError) as context:
            run_convert(opts)

        self.assertIn("File not found: fake.json", str(context.exception))
