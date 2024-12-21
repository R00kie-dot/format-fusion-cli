import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from formatfusion.commands.cmd_image import get_image_path, get_output_path, run_convert


class TestFormatFusionImage(unittest.TestCase):
    @patch("formatfusion.commands.cmd_image.get_image_path")
    @patch("formatfusion.commands.cmd_image.get_output_path")
    @patch("formatfusion.core.image.ConverterImage.convert_image_to_base64")
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

        os.remove(image_path)
        os.remove(output_path)

    def test_get_image_path_valid(self):
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_image:
            temp_image_path = temp_image.name
        opts = {"<path>": temp_image_path}
        result = get_image_path(opts)
        self.assertEqual(result, Path(temp_image_path))
        os.remove(temp_image_path)

    def test_get_image_path_invalid(self):
        opts = {"<path>": "nonexistent.png"}
        with self.assertRaises(FileNotFoundError):
            get_image_path(opts)

    def test_with_output_specified(self):
        opts = {"--output": "/tmp/specified_output.txt"}
        result = get_output_path(opts)
        expected = Path("/tmp/specified_output.txt").resolve()
        self.assertEqual(result, expected)

    def test_with_no_output_specified(self):
        opts = {"--output": None}
        result = get_output_path(opts)
        expected = Path("output.txt").resolve()
        self.assertEqual(result, expected)

    def test_relative_path_output(self):
        opts = {"--output": "relative_output.txt"}
        result = get_output_path(opts)
        expected = Path("relative_output.txt").resolve()
        self.assertEqual(result, expected)

    def test_default_output(self):
        opts = {"--output": "output.txt"}
        result = get_output_path(opts)
        expected = Path("output.txt").resolve()
        self.assertEqual(result, expected)

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
