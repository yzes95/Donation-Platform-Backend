"""Family cases and directory routes."""
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from database.connection import get_db
from schemas.family import FamilyCreate, FamilyUpdate, FamilyResponse, FamilyGroupResponse

router = APIRouter()


@router.get("/", response_model=List[FamilyResponse])
async def list_families(
    category: Optional[str] = None,
    governorate: Optional[str] = None,
    group_id: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """List verified family cases with optional filtering."""
    # Wireframe placeholder
    return []


@router.get("/groups", response_model=List[FamilyGroupResponse])
async def list_family_groups(db: AsyncSession = Depends(get_db)):
    """List registered family lineages and tribal groups."""
    # Wireframe placeholder
    return []


@router.get("/{family_id}", response_model=FamilyResponse)
async def get_family_details(family_id: str, db: AsyncSession = Depends(get_db)):
    """Get single family case details by ID."""
    # Wireframe placeholder
    raise HTTPException(status_code=404, detail="Family not found")


@router.post("/", response_model=FamilyResponse, status_code=status.HTTP_201_CREATED)
async def create_family_case(family_in: FamilyCreate, db: AsyncSession = Depends(get_db)):
    """Submit a new family case for field verification."""
    # Wireframe placeholder
    raise HTTPException(status_code=501, detail="Not implemented yet")


@router.patch("/{family_id}", response_model=FamilyResponse)
async def update_family_case(family_id: str, family_update: FamilyUpdate, db: AsyncSession = Depends(get_db)):
    """Update family case details (Representative or Admin)."""
    # Wireframe placeholder
    raise HTTPException(status_code=501, detail="Not implemented yet")
