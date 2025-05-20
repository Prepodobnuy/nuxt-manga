from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from .auth import router as auth_router
from .user import router as user_router
from .title import router as title_router
from .person import router as person_router
from .tags import router as tags_router
from .asset import router as asset_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

router = APIRouter(prefix="/api")

router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(user_router)
router.include_router(title_router, prefix="/title", tags=["Title"])
router.include_router(person_router, prefix="/person", tags=["Person"])
router.include_router(asset_router, prefix="/asset", tags=["Asset"])

router.include_router(tags_router)
app.include_router(router)


def run():
    import uvicorn

    uvicorn.run(app="routes:app", workers=20, reload=True)
    ...
