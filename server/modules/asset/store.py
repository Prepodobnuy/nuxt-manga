import os
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import List

from PIL import Image
from pydantic import BaseModel


class StoreMetaModel(BaseModel):
    auto_increment_value: int


@dataclass
class AssetStore:
    basepath: str
    dirs: List[str]
    model: BaseModel
    size: tuple[int, int] | None = None

    def __post_init__(self):
        self.__check_dirs()
        self.__check_files()
        self.__check_models()
        self.__check_meta()

    def __check_dirs(self):
        path = Path(self.basepath)

        for dir_name in self.dirs:
            path = path / dir_name
            if not path.exists():
                path.mkdir(parents=True, exist_ok=True)

        schema_path = path / "schema"
        if not schema_path.exists():
            schema_path.mkdir()
        meta_path = path / "meta"
        if not schema_path.exists():
            meta_path.mkdir()

    def __check_files(self):
        target_path = self.__get_path()
        self.entities = len([
            entry.name
            for entry in os.scandir(target_path)
            if entry.is_file() and entry.name.endswith(".png")
        ])

    def __check_models(self):
        models_path = self.__get_models_path()
        self.models_count = len([
            entry.name
            for entry in os.scandir(models_path)
            if entry.is_file() and entry.name.endswith(".json")
        ])

    def __check_meta(self):
        meta_path = self.__get_meta_path()
        if not meta_path.exists():
            meta = StoreMetaModel(auto_increment_value=0)
            with open(meta_path, 'w') as metaf:
                metaf.write(meta.model_dump_json())

    def increment_name(self) -> str:
        meta_path = self.__get_meta_path()
        with open(meta_path, 'r') as metaf:
            meta = StoreMetaModel.model_validate_json(metaf.read())
        res = str(meta.auto_increment_value)
        meta.auto_increment_value += 1
        with open(meta_path, 'w') as metaf:
            metaf.write(meta.model_dump_json())
        return res

    def __get_path(self) -> Path:
        return Path(self.basepath).joinpath(*self.dirs)

    def __get_models_path(self) -> Path:
        return self.__get_path() / "schema"

    def __get_meta_path(self) -> Path:
        return self.__get_path() / "meta" / "meta.json"

    def set(self, filename: str, content: bytes, scheme: BaseModel):
        asset_path = self.__get_path() / f"{filename}.png"
        with Image.open(BytesIO(content)) as img:
            if self.size:
                img = img.resize(self.size)
            img.save(asset_path)

        model_path = self.__get_models_path() / f"{filename}.json"
        with open(model_path, "w") as f:
            f.write(scheme.model_dump_json())

    def delete(self, filename: str):
        asset_path = self.__get_path() / f"{filename}.png"
        model_path = self.__get_models_path() / f"{filename}.json"

        if os.path.exists(asset_path):
            os.remove(asset_path)
        if os.path.exists(model_path):
            os.remove(model_path)

    def clear(self):
        for en in os.scandir(self.__get_path()):
            if os.path.isfile(en):
                os.remove(en)

        for en in os.scandir(self.__get_models_path()):
            if os.path.isfile(en):
                os.remove(en)

    def list_assets(self):
        return [
            en
            for en in os.scandir(self.__get_path())
            if os.path.isfile(en)
        ]

    def list_models(self):
        res = []
        for en in os.scandir(self.__get_models_path()):
            if os.path.isfile(en):
                with open(en, 'r') as file:
                    res.append(self.model.model_validate_json(file.read()))
        return res

    def list_names(self):
        return [
            en
            for en in os.listdir(self.__get_models_path())
        ]

    def get_content(self, filename: str) -> bytes | None:
        asset_path = self.__get_path() / f"{filename}.png"
        if not asset_path.exists():
            return None
        with open(asset_path, "rb") as f:
            return f.read()

    def get_model(self, filename: str) -> BaseModel | None:
        model_path = self.__get_models_path() / f"{filename}.json"
        if not model_path.exists():
            return None
        with open(model_path, "r") as f:
            return self.model.model_validate_json(f.read())
