"""FastAPI application for Energy Platform."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.buildings import router as buildings_router
from app.api.health import router as health_router
from app.core.config import settings
from app.core.database import Base, engine

print("\n🔧 Energy Platform API Starting up...")

app = FastAPI(
    title="Energy Platform API",
    description="AI-powered energy consumption analysis and recommendations",
    version="0.1.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5175",  # Dev frontend
        "http://localhost:3000",  # Alt dev frontend
        "http://localhost:5173",  # Other frontend
        "http://localhost:5174",  # Other frontend
        "https://example.com",  # Production frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health_router)
app.include_router(buildings_router)

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Energy Platform API v0.1.0", "status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
    )

if settings.environment == "development":
    app.include_router(dev_router)


@app.get("/")
async def root() -> dict:
    """Root endpoint."""
    return {"message": "AI Full-Stack Starter API"}
