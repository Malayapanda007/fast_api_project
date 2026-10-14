from app.core.security import verify_access_token
from fastapi import HTTPException,Header
import traceback


def get_current_user(token:str=Header(...))->str:
    user=verify_access_token(token)
    if not user:
        raise HTTPException(status_code=401,detail='Invalid token')
    return user
