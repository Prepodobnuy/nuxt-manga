import uvicorn

from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from database.tables import initialize
from api import app

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HOST = 'localhost'
PORT = 8000

if __name__ == '__main__':
    initialize()
    uvicorn.run(
        "main:app",
        reload=True,
        host=HOST,
        port=PORT,
    )
