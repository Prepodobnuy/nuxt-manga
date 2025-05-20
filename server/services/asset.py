from dataclasses import dataclass
from io import BytesIO
import os

from PIL import Image

from config.assets import ASSETS_PATH

# ASSETS_PATH = "/home/prepodobnuy/.sdc/assets"


@dataclass
class AssetService:
    path: str
    size: tuple[int, int] | None = None

    def set(self, value: bytes):
        path = f"{ASSETS_PATH}/{self.path}"
        print("\n\n\n\n", path)
        with BytesIO(value) as content:
            image = Image.open(content)
            if self.size is not None:
                image = image.resize(self.size)
            image.save(path)

    def get(self) -> bytes | None:
        path = f"{ASSETS_PATH}/{self.path}"
        if os.path.exists(path):
            with open(path, 'rb') as content:
                return content.read()

    def clear(self):
        path = f"{ASSETS_PATH}/{self.path}"
        if os.path.exists(path):
            os.remove(path)

    def exist(self):
        path = f"{ASSETS_PATH}/{self.path}"
        return os.path.exists(path)

    def full_path(self):
        return f"{ASSETS_PATH}/{self.path}"
