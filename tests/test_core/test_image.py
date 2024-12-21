import base64
import unittest
from pathlib import Path
from unittest.mock import mock_open, patch

from formatfusion.core.image import ConverterImage


class TestConvertImage(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data=b"test_image_data")
    @patch("formatfusion.core.base.Base.save_result")
    def test_convert_image_to_base64(self, mock_save_result, mock_open):
        input_file = Path("/path/to/input/image.jpg")
        output_file = Path("/path/to/output/image_base64.txt")
        converter = ConverterImage(input_file=input_file, output_file=output_file)

        expected_base64_result = base64.b64encode(b"test_image_data").decode("utf-8")

        converter.convert_image_to_base64()

        mock_save_result.assert_called_once_with(
            expected_base64_result, f"The converted image was saved in {output_file}"
        )
