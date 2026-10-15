import os, secrets
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import create_access_token

router = APIRouter()

@router.post('/login')
def login(form: OAuth2PasswordRequestForm = Depends()):
    user_ok = secrets.compare_digest(form.username, os.getenv("ADMIN_USER", "admin"))
    pass_ok = secrets.compare_digest(form.password, os.getenv("ADMIN_PASSWORD", "admin"))
    if not (user_ok and pass_ok):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token({'sub': form.username})
    return {"access_token": token, "token_type": "bearer"}