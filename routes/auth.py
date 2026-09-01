"""Authentication and user management routes."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database.connection import get_db
from schemas.user import UserCreate, UserLogin, UserResponse, Token

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    """Register a new family representative or donor."""
    # Wireframe placeholder
    raise HTTPException(status_code=501, detail="Not implemented yet")


@router.post("/login", response_model=Token)
async def login(login_data: UserLogin, db: AsyncSession = Depends(get_db)):
    """Authenticate user and return JWT access token."""
    # Wireframe placeholder
    raise HTTPException(status_code=501, detail="Not implemented yet")


@router.get("/me", response_model=UserResponse)
async def get_current_user_profile():
    """Retrieve currently authenticated user profile."""
    # Wireframe placeholder
    raise HTTPException(status_code=501, detail="Not implemented yet")
