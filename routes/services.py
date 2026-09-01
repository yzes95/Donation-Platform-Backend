"""Assistance Needs and Services routes."""
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database.connection import get_db
from schemas.service import NeedCreate, NeedUpdate, NeedResponse

router = APIRouter()


@router.get("/", response_model=List[NeedResponse])
async def list_services(family_id: Optional[str] = None, category: Optional[str] = None, db: AsyncSession = Depends(get_db)):
    """List assistance needs with optional family or category filter."""
    # Wireframe placeholder
    return []


@router.get("/{need_id}", response_model=NeedResponse)
async def get_service_details(need_id: str, db: AsyncSession = Depends(get_db)):
    """Get assistance need details."""
    # Wireframe placeholder
    raise HTTPException(status_code=404, detail="Need item not found")


@router.post("/", response_model=NeedResponse, status_code=status.HTTP_201_CREATED)
async def create_service_need(need_in: NeedCreate, db: AsyncSession = Depends(get_db)):
    """Create a new assistance need item for a family."""
    # Wireframe placeholder
    raise HTTPException(status_code=501, detail="Not implemented yet")
