from io import BytesIO

from PIL import Image

from config.assets import ASSETS_PATH


def get_asset_name(cathegory: str, resolution: str, unique_str: str) -> str:
    return f"{cathegory}.{resolution}.{unique_str}"


def get_asset_path(filename: str) -> str:
    return f"{ASSETS_PATH}/{filename}"


def get_asset(
    path_or_bytes: str | BytesIO, size: tuple[int, int] | None
) -> Image.Image:
    try:
        with Image.open(path_or_bytes) as image:
            if size is None:
                return image.copy()
            return image.resize(size)
    except IOError as e:
        raise Exception(f"{e}")


def load_asset(path: str) -> bytes:
    try:
        with open(path, "rb") as file:
            return file.read()
    except Exception:
        raise FileNotFoundError()
