"""Payment Gateway Webhooks and Processing routes."""
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from database.connection import get_db
from schemas.payment import PaymentInitiateRequest, PaymentInitiateResponse

router = APIRouter()


@router.post("/initiate", response_model=PaymentInitiateResponse)
async def initiate_payment(payment_in: PaymentInitiateRequest, db: AsyncSession = Depends(get_db)):
    """Initiate payment via InstaPay, Vodafone Cash, Fawry, or Card gateway."""
    # Wireframe placeholder
    raise HTTPException(status_code=501, detail="Not implemented yet")


@router.post("/webhook/{gateway}")
async def payment_webhook(gateway: str, request: Request, db: AsyncSession = Depends(get_db)):
    """Process incoming payment gateway webhook notification."""
    # Wireframe placeholder
    return {"status": "received", "gateway": gateway}
