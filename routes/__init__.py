"""API Routes package."""
from fastapi import APIRouter
from .auth import router as auth_router
from .families import router as families_router
from .services import router as services_router
from .donations import router as donations_router
from .payments import router as payments_router
from .admin import router as admin_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
api_router.include_router(families_router, prefix="/families", tags=["Families"])
api_router.include_router(services_router, prefix="/services", tags=["Services & Needs"])
api_router.include_router(donations_router, prefix="/donations", tags=["Donations"])
api_router.include_router(payments_router, prefix="/payments", tags=["Payments & Gateways"])
api_router.include_router(admin_router, prefix="/admin", tags=["Admin & Governance"])

__all__ = ["api_router"]
