"""Family Case Pydantic Schemas."""
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from models.family import FamilyStatus, UrgencyLevel


class FamilyGroupResponse(BaseModel):
    id: str
    name_ar: str
    name_en: str
    region_ar: str
    region_en: str

    model_config = ConfigDict(from_attributes=True)


class FamilyBase(BaseModel):
    name_ar: str
    name_en: str
    family_group_id: Optional[str] = None
    governorate_ar: str
    governorate_en: str
    members_count: int = 1
    monthly_income: float = 0.0
    social_status_ar: Optional[str] = None
    social_status_en: Optional[str] = None
    housing_status_ar: Optional[str] = None
    housing_status_en: Optional[str] = None
    summary_ar: Optional[str] = None
    summary_en: Optional[str] = None
    urgency: UrgencyLevel = UrgencyLevel.HIGH


class FamilyCreate(FamilyBase):
    pass


class FamilyUpdate(BaseModel):
    name_ar: Optional[str] = None
    name_en: Optional[str] = None
    monthly_income: Optional[float] = None
    housing_status_ar: Optional[str] = None
    status: Optional[FamilyStatus] = None
    urgency: Optional[UrgencyLevel] = None


class FamilyResponse(FamilyBase):
    id: str
    code: str
    status: FamilyStatus
    verified_at: Optional[datetime] = None
    verified_by_ar: Optional[str] = None
    verified_by_en: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
