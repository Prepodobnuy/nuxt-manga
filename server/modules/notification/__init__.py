from typing import Literal, Type, TypeAlias

NotificationType: TypeAlias = Literal[
    "title_new_volume",
    "title_new_meta",
    "title_new_cover",
]


class Notification:
    # title notifications
    @staticmethod
    def title_new_volume(title_id: int, volume_id: int) -> dict:
        return {
            "type": "title_new_volume",
            "title_id": title_id,
            "volume_id": volume_id,
        }

    # for moderators/admins only
    @staticmethod
    def title_new_meta(title_id: int, meta_id: int) -> dict:
        return {
            "type": "title_new_meta",
            "title_id": title_id,
            "meta_id": meta_id,
        }

    # for moderators/admins only
    @staticmethod
    def title_new_cover(title_id: int, cover_id: int) -> dict:
        return {
            "type": "title_new_cover",
            "title_id": title_id,
            "cover_id": cover_id,
        }
