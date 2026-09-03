from pydantic import BaseModel


class PaymentInitiateRequest(BaseModel):
    donation_id: str
    payment_method: str


class PaymentInitiateResponse(BaseModel):
    status: str
    reference_code: str

# TODO: Add payment webhook payload and provider schemas
