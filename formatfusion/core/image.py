import base64
from pathlib import Path

from formatfusion.models.file_converter_model import FileConverterModel
from .base import Base


class ConverterImage(Base):
    def __init__(self, input_file: Path, output_file: Path):
        super().__init__(input_file, output_file)
        validated_data = FileConverterModel(
            input_file=Path(input_file),
            output_file=Path(output_file) if output_file else None,
        )
        self.input_file = validated_data.input_file
        self.output_file = validated_data.output_file

    def convert_image_to_base64(self) -> None:
        with open(self.input_file, "rb") as image:
            result = base64.b64encode(image.read()).decode("utf-8")
            self.save_result(
                result, f"The converted image was saved in {self.output_file.as_uri()}"
            )
