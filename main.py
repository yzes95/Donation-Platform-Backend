from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.settings import settings
from routes.admin import router as admin_router

app = FastAPI(
    title=settings.APP_NAME,
    description="Ataa (عطاء) — Family Donation Management Platform API",
    version="1.0.0",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Admin test routes
app.include_router(admin_router, prefix="/api/v1/admin", tags=["Admin"])


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check for AWS ALB / ECS Target Groups."""
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "env": settings.APP_ENV,
    }


# TODO: Include additional routers as you build them:
# from routes.auth import router as auth_router
# from routes.families import router as families_router
# from routes.services import router as services_router
# from routes.donations import router as donations_router
# from routes.payments import router as payments_router
# app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])
# app.include_router(families_router, prefix="/api/v1/families", tags=["Families"])
# app.include_router(services_router, prefix="/api/v1/services", tags=["Services"])
# app.include_router(donations_router, prefix="/api/v1/donations", tags=["Donations"])
# app.include_router(payments_router, prefix="/api/v1/payments", tags=["Payments"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main.py:app", host="0.0.0.0", port=8000, reload=True)
