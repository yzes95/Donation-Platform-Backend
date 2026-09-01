"""Payment Gateway Pydantic Schemas."""
from typing import Optional, Dict, Any
from pydantic import BaseModel
from models.donation import PaymentMethod


class PaymentInitiateRequest(BaseModel):
    donation_id: str
    payment_method: PaymentMethod
    return_url: Optional[str] = None


class PaymentInitiateResponse(BaseModel):
    payment_url: Optional[str] = None
    qr_code_data: Optional[str] = None
    reference_code: str
    status: str


class WebhookPayload(BaseModel):
    gateway: str
    event: str
    data: Dict[str, Any]
