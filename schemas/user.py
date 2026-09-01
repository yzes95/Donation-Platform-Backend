"""User and Authentication Pydantic Schemas."""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict
from models.user import Role


class UserBase(BaseModel):
    email: EmailStr
    full_name_ar: str
    full_name_en: Optional[str] = None
    phone_number: Optional[str] = None
    role: Role = Role.FAMILY_REP


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(UserBase):
    id: int
    is_active: bool
    is_verified: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: str
    user_id: int


class TokenData(BaseModel):
    email: Optional[str] = None
    role: Optional[str] = None
