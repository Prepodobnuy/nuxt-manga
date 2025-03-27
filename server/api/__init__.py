from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse

from .auth import router as auth_router
from .user import router as user_router
from .title import router as title_router
from .person import router as person_router
from etc.static import tags, genres

app = FastAPI()

app.include_router(auth_router, prefix='/auth', tags=['Auth'])
app.include_router(user_router, prefix='/user', tags=['User'])
app.include_router(title_router, prefix='/title', tags=['Title'])
app.include_router(person_router, prefix='/person', tags=['Person'])


@app.get('/tags')
async def get_tags():
    return tags


@app.get('/genres')
async def get_genres():
    return genres
