import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from formatfusion.commands.cmd_yaml import (
    get_input_file_path,
    get_output_file_path,
    run_convert,
)


class TestFormatFusionYaml(unittest.TestCase):
    @patch("pathlib.Path.exists")
    def test_get_input_file_path_file_exists(self, mock_exists):
        mock_exists.return_value = True

        opts = {"<path>": "/path/to/input/file.json"}
        result = get_input_file_path(opts)
        self.assertEqual(result, Path("/path/to/input/file.json").resolve())

    @patch("pathlib.Path.exists")
    def test_get_input_file_path_file_not_found(self, mock_exists):
        mock_exists.return_value = False

        opts = {"<path>": "/path/to/input/file.json"}
        with self.assertRaises(FileNotFoundError):
            get_input_file_path(opts)

    @patch("pathlib.Path.exists")
    def test_get_output_file_path_with_custom_output(self, mock_exists):
        mock_exists.return_value = True
        opts = {
            "--output": "/path/to/output/file.yaml",
            "<path>": "/path/to/input/file.json",
        }
        input_file = Path("/path/to/input/file.json")

        result = get_output_file_path(opts, input_file)
        self.assertEqual(result, Path("/path/to/output/file.yaml").resolve())

    @patch("pathlib.Path.exists")
    def test_get_output_file_path_with_default_output(self, mock_exists):
        mock_exists.return_value = True
        opts = {"--output": None, "<path>": "/path/to/input/file.json"}
        input_file = Path("/path/to/input/file.json")

        result = get_output_file_path(opts, input_file)
        self.assertEqual(result, Path("/path/to/input/output.yaml").resolve())

    @patch("pathlib.Path.exists")
    def test_get_output_file_path_with_invalid_extension(self, mock_exists):
        mock_exists.return_value = True
        opts = {"--output": None, "<path>": "/path/to/input/file.txt"}
        input_file = Path("/path/to/input/file.txt")

        with self.assertRaises(ValueError):
            get_output_file_path(opts, input_file)
