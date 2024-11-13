import os
import tempfile
import unittest
from unittest.mock import patch

from formatfusion.commands.cmd_image import get_image_path, get_output_path, run_convert


class TestFormatFusionImage(unittest.TestCase):
    @patch("formatfusion.commands.cmd_image.get_image_path")
    @patch("formatfusion.commands.cmd_image.get_output_path")
    @patch("formatfusion.converter.Converter.convert_image_to_base64")
    def test_run_convert_success(
        self, mock_convert_image_to_base64, mock_get_output_path, mock_get_image_path
    ):
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_image:
            image_path = temp_image.name
        with tempfile.NamedTemporaryFile(delete=False) as temp_output:
            output_path = temp_output.name

        mock_get_image_path.return_value = image_path
        mock_get_output_path.return_value = output_path

        mock_convert_image_to_base64.return_value = "base64_encoded_data"

        opts = {"<path>": image_path, "--output": output_path}
        run_convert(opts)

        mock_convert_image_to_base64.assert_called_once()
        with open(output_path, "r") as file:
            content = file.read()
            self.assertEqual(content, "base64_encoded_data")

        os.remove(image_path)
        os.remove(output_path)

    def test_get_image_path_valid(self):
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_image:
            temp_image_path = temp_image.name
        opts = {"<path>": temp_image_path}
        result = get_image_path(opts)
        self.assertEqual(result, os.path.abspath(temp_image_path))
        os.remove(temp_image_path)

    def test_get_image_path_invalid(self):
        opts = {"<path>": "nonexistent.png"}
        with self.assertRaises(FileNotFoundError):
            get_image_path(opts)

    def test_get_output_path(self):
        opts = {"--output": "custom_output.txt"}
        result = get_output_path(opts)
        self.assertEqual(result, os.path.abspath("custom_output.txt"))

        opts = {"--output": None}
        result = get_output_path(opts)
        self.assertEqual(result, os.path.abspath("output.txt"))

    @patch(
        "formatfusion.commands.cmd_image.get_image_path",
        side_effect=FileNotFoundError("File not found: fake_image.png"),
    )
    @patch("formatfusion.commands.cmd_image.get_output_path", return_value="output.txt")
    def test_run_convert_file_not_found(self, mock_output, mock_image_path):
        opts = {"<path>": "fake_image.png", "--output": "output.txt"}
        with self.assertRaises(FileNotFoundError) as context:
            run_convert(opts)
        self.assertIn("File not found: fake_image.png", str(context.exception))


if __name__ == "__main__":
    unittest.main()
