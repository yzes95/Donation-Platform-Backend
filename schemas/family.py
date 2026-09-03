from typing import Optional
from pydantic import BaseModel


class FamilyBase(BaseModel):
    name_ar: str
    name_en: str
    governorate: str
    urgency: str = "high"


class FamilyCreate(FamilyBase):
    pass


class FamilyResponse(FamilyBase):
    id: str
    code: str
    status: str

    class Config:
        from_attributes = True

# TODO: Add FamilyUpdate, FamilyGroupResponse, and verification schemas
