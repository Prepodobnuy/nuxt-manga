from dataclasses import dataclass

from models.title.meta import TitleMeta
from models.user.user import User
from services.title.meta import TitleMetaService


@dataclass
class ModerService:
    user: User

    async def approve_meta(self, meta: TitleMeta):
        ser = TitleMetaService(meta)
        await ser.approve(user=self.user)

    async def decline_meta(self, meta: TitleMeta):
        ser = TitleMetaService(meta)
        await ser.decline(user=self.user)
