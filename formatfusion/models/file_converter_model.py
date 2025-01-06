import os
from pathlib import Path

from pydantic import BaseModel, field_validator, model_validator

VALID_EXTENSIONS = {"json", "yaml", "png", "jpg"}


class FileConverterModel(BaseModel):
    input_file: Path
    output_file: Path | None = None

    @field_validator("input_file")
    def validate_input_file(cls, value: Path) -> Path:
        if not os.path.isfile(value):
            raise ValueError(f"The input file '{value}' does not exist.")
        if value.suffix.lstrip(".") not in VALID_EXTENSIONS:
            raise ValueError(
                f"Invalid input file format '{value.suffix.lstrip('.')}'. "
                f"Acceptable formats: {', '.join(VALID_EXTENSIONS)}."
            )
        return value

    @model_validator(mode="after")
    def validate_file_pair(self):
        if self.output_file:
            input_ext = self.input_file.suffix.lstrip(".")
            output_ext = self.output_file.suffix.lstrip(".")
            if input_ext == "json" and output_ext != "yaml":
                raise ValueError(
                    "For a JSON input file, the output file must have the extension '.yaml'."
                )
            if input_ext == "yaml" and output_ext != "json":
                raise ValueError(
                    "For a YAML input file, the output file must have the extension '.json'."
                )
        return self
