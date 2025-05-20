from fastapi import APIRouter

from .person import router as person_router
from .meta import router as meta_router


router = APIRouter()

router.include_router(person_router, tags=[])
router.include_router(meta_router, prefix="/meta", tags=[])
