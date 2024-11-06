import unittest
from unittest.mock import patch, mock_open

from formatfusion.converting import Converting


class TestConvertJsonToYaml(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value", "nested": {"key2": "value2"}}')
    @patch("json.load")
    @patch("yaml.dump")
    def test_convert_json_to_yaml(self, mock_yaml_dump, mock_json_load, mock_open):
        mock_json_load.return_value = {"key": "value", "nested": {"key2": "value2"}}
        mock_yaml_dump.return_value = "key: value\nnested:\n  key2: value2\n"

        converter = Converting("test.json")
        result = converter.convert_json_to_yaml()


        mock_open.assert_called_once_with("test.json", "r", encoding="utf-8")
        mock_json_load.assert_called_once()
        mock_yaml_dump.assert_called_once_with({"key": "value", "nested": {"key2": "value2"}}, sort_keys=False)
        self.assertEqual(result, "key: value\nnested:\n  key2: value2\n")

    @patch("builtins.open", new_callable=mock_open, read_data=b"image_data")
    @patch("base64.b64encode")
    def test_convert_image_to_base64(self, mock_b64encode, mock_open):
        mock_b64encode.return_value = b"encoded_image_data"

        converter = Converting("test_image.jpg")
        result = converter.convert_image_to_base64()


        mock_open.assert_called_once_with("test_image.jpg", "rb")
        mock_b64encode.assert_called_once_with(b"image_data")
        self.assertEqual(result, "encoded_image_data")
