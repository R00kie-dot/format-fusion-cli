import unittest
from pathlib import Path

from formatfusion.helpers import get_file_extension


class TestGetFileExtension(unittest.TestCase):
    def test_valid_extensions(self):
        self.assertEqual(get_file_extension(Path("example.txt")), "txt")
        self.assertEqual(get_file_extension(Path("archive.tar.gz")), "gz")
        self.assertEqual(get_file_extension(Path("photo.jpeg")), "jpeg")

    def test_no_extension(self):
        self.assertEqual(get_file_extension(Path("file")), "")

    def test_hidden_file(self):
        self.assertEqual(get_file_extension(Path(".hiddenfile")), "")

    def test_complex_extensions(self):
        self.assertEqual(get_file_extension(Path("complex.name.with.dots.csv")), "csv")

    def test_directory(self):
        self.assertEqual(get_file_extension(Path("folder/")), "")

    def test_empty_filename(self):
        with self.assertRaises(ValueError):
            get_file_extension(Path(""))
