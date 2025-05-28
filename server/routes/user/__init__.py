from fastapi import APIRouter
from .user import router as user_router
from .puts import router as puts_router
from .moder import router as moder_router
from .admin import router as admin_router

router = APIRouter()

router.include_router(router=user_router, prefix="", tags=["User"])
router.include_router(router=puts_router, prefix="", tags=["User"])
router.include_router(router=moder_router, prefix="/moder", tags=["Mod"])
router.include_router(router=admin_router, prefix="/admin", tags=["Admin"])
