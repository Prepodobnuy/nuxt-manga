from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from fastapi import UploadFile, File
from database.session import get_session
from auth.auth import get_current_user

session = get_session()