from pydantic import BaseModel
from config.assets import ASSETS_PATH, TITLE_COVER_RESOLUTION
from .store import AssetStore


PENDING_LIMIT = 50


class CoverModel(BaseModel):
    approved: bool
    order: int
    posted_user_uuid: str


class TitleAssetStore:
    def __init__(self, id: int):
        self.covers = AssetStore(
            basepath=ASSETS_PATH,
            dirs=["title", str(id), "cover"],
            model=CoverModel,
            size=TITLE_COVER_RESOLUTION,
        )
        self.id = str(id)

    def list_pending_models(self):
        return [
            m
            for m in self.covers.list_models()
            if not m.approved == False
        ]

    def list_approved_models(self):
        return [
            m
            for m in self.covers.list_models()
            if m.approved
        ]

    def add_cover(self, content: bytes, uuid: str, order: int):
        if len(self.list_pending_models()) >= PENDING_LIMIT:
            raise Exception

        self.covers.set(
            content=content,
            filename=self.covers.increment_name(),
            scheme=CoverModel(approved=False, order=order,
                              posted_user_uuid=uuid)
        )

    def clear(self):
        self.covers.clear()
