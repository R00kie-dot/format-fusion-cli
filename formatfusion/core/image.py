import base64

from .base import Base


class ConverterImage(Base):

    def convert_image_to_base64(self) -> None:
        with open(self.input_file, "rb") as image:
            result = base64.b64encode(image.read()).decode("utf-8")
            self.save_result(
                result,
                f"The converted image was saved in {self.output_file}"
            )
