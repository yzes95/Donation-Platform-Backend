"""Donation Pydantic Schemas."""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict
from models.donation import DonationType, DonationStatus, PaymentMethod


class DonationCreate(BaseModel):
    type: DonationType = DonationType.FAMILY
    family_id: Optional[str] = None
    need_id: Optional[str] = None
    amount: float
    platform_tip: float = 0.0
    is_anonymous: bool = False
    donor_name_ar: Optional[str] = None
    donor_name_en: Optional[str] = None
    donor_email: Optional[EmailStr] = None
    donor_phone: Optional[str] = None
    payment_method: PaymentMethod


class DonationResponse(BaseModel):
    id: str
    reference_id: str
    type: DonationType
    family_id: Optional[str] = None
    need_id: Optional[str] = None
    amount: float
    platform_tip: float
    total_paid: float
    is_anonymous: bool
    donor_name_ar: Optional[str] = None
    payment_method: PaymentMethod
    status: DonationStatus
    created_at: datetime
    delivered_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class DonationTrackResponse(BaseModel):
    reference_id: str
    status: DonationStatus
    amount: float
    type: DonationType
    target_name_ar: Optional[str] = None
    target_name_en: Optional[str] = None
    created_at: datetime
    delivered_at: Optional[datetime] = None
