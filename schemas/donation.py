from typing import Optional
from pydantic import BaseModel


class DonationCreate(BaseModel):
    family_id: Optional[str] = None
    amount: float
    payment_method: str
    is_anonymous: bool = False


class DonationResponse(BaseModel):
    id: str
    reference_id: str
    amount: float
    status: str

    class Config:
        from_attributes = True

# TODO: Add DonationTrackResponse and donor detail schemas
