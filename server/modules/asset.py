import os

from dataclasses import dataclass
from PIL import Image
from pydantic import BaseModel


@dataclass
class AssetStore:
    dir: str
    model: BaseModel
    size: tuple[int, int] | None = None
    limit: int | None = None

    def __post_init__(self):
        self.__check_dirs()

    def __check_dirs(self):
        if os.path.exists(self.dir):
            if os.path.exists(f"self.dir/schema"):
                return

        for d in self.dir.split("/"):
            os.mkdir(d)
        os.mkdir(f"{self.dir}/schema")

    def __get_content(self) -> list[str]:
        entries = [
            e
            for e in os.listdir(self.dir)
            if os.path.isfile(e)
        ]
        return entries

    def __check_content(self):
        content = self.__get_content()
        if self.limit is not None:
            if len(content) >= self.limit:
                raise ValueError

    def set(self, filename: str, bytes: bytes, model):
        self.__check_content()
        path = f"{self.dir}/{filename}"

        with Image.open(bytes) as img:
            if self.size is not None:
                img = img.resize(self.size)
            img.save(path)

    def __set_scheme(self, filename: str, scheme: BaseModel):
        path = f"{self.dir}/schema/{filename}"
        content = scheme.model_dump_json()
        with open(path, 'w') as file:
            file.write(content)

    def get(self, filename: str) -> bytes | None:
        path = f"{self.dir}/{filename}"

        if not os.path.exists(path):
            return None

        with open(path, 'rb') as img:
            return img.read()

    def get_scheme(self, filename: str, scheme: BaseModel) ->:
        path = f"{self.dir}/schema/{filename}"
        with open(path, 'w') as file:
            file.write(content)
