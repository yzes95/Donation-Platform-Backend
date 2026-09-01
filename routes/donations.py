"""Donations and Tracking routes."""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database.connection import get_db
from schemas.donation import DonationCreate, DonationResponse, DonationTrackResponse

router = APIRouter()


@router.post("/", response_model=DonationResponse, status_code=status.HTTP_201_CREATED)
async def create_donation(donation_in: DonationCreate, db: AsyncSession = Depends(get_db)):
    """Initiate a donation pledge and generate an official reference ID."""
    # Wireframe placeholder
    raise HTTPException(status_code=501, detail="Not implemented yet")


@router.get("/track/{reference_id}", response_model=DonationTrackResponse)
async def track_donation(reference_id: str, db: AsyncSession = Depends(get_db)):
    """Track donation lifecycle by reference ID."""
    # Wireframe placeholder
    raise HTTPException(status_code=404, detail="Donation reference not found")


@router.get("/history", response_model=List[DonationResponse])
async def get_donation_history(db: AsyncSession = Depends(get_db)):
    """Get authenticated user donation history."""
    # Wireframe placeholder
    return []
