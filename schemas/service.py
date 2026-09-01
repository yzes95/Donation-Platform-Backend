"""Assistance Need / Service Pydantic Schemas."""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from models.service import NeedCategory, NeedStatus


class NeedBase(BaseModel):
    family_id: str
    title_ar: str
    title_en: str
    category: NeedCategory
    unit_label_ar: Optional[str] = None
    unit_label_en: Optional[str] = None
    target_amount: float
    description_ar: Optional[str] = None
    description_en: Optional[str] = None
    beneficiary_ar: Optional[str] = None
    beneficiary_en: Optional[str] = None


class NeedCreate(NeedBase):
    pass


class NeedUpdate(BaseModel):
    title_ar: Optional[str] = None
    target_amount: Optional[float] = None
    status: Optional[NeedStatus] = None
    description_ar: Optional[str] = None


class NeedResponse(NeedBase):
    id: str
    code: str
    raised_amount: float
    status: NeedStatus
    donors_count: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
