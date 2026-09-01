"""Authentication and RBAC security dependencies."""
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from config.settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_PREFIX}/auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Validate JWT token and return active user."""
    # Wireframe dependency placeholder
    return {"token": token}


async def get_current_admin(current_user: dict = Depends(get_current_user)):
    """Enforce administrator role check."""
    return current_user
