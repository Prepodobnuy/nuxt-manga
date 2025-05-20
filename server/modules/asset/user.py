from pydantic import BaseModel
from config.assets import ASSETS_PATH, USER_BACK_RESOLUTION, USER_PFP_RESOLUTION
from .store import AssetStore


class UserPfpModel(BaseModel):
    uuid: str


class UserBackModel(BaseModel):
    uuid: str


class UserAssetStore:
    def __init__(self, uuid: str):
        self.pfp = AssetStore(
            basepath=ASSETS_PATH,
            dirs=["user", uuid, "pfp"],
            model=UserPfpModel,
            size=USER_PFP_RESOLUTION,
        )
        self.back = AssetStore(
            basepath=ASSETS_PATH,
            dirs=["user", uuid, "back"],
            model=UserBackModel,
            size=USER_BACK_RESOLUTION,
        )
        self.uuid = uuid

    def get_pfp(self) -> bytes | None:
        return self.pfp.get_content("asset")

    def get_back(self) -> bytes | None:
        return self.back.get_content("asset")

    def set_pfp(self, content: bytes):
        self.pfp.set("asset", content, UserPfpModel(uuid=self.uuid))

    def set_back(self, content: bytes):
        self.back.set("asset", content, UserBackModel(uuid=self.uuid))

    def clear(self):
        self.pfp.clear()
        self.back.clear()
