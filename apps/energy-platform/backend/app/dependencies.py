"""API dependencies for FastAPI."""

from fastapi import HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import AsyncSessionLocal, get_db as get_db_async
from app.core.config import settings
import uuid

security = HTTPBearer()


async def get_db() -> AsyncSession:
    """Get async database session."""
    async with AsyncSessionLocal() as session:
        yield session


async def get_current_user(credentials: HTTPAuthCredentials) -> dict:
    """
    Extract user from auth credentials.
    In production, verify JWT token from Supabase Auth.
    For testing, accept a placeholder UUID.
    """
    # For now, accept any Bearer token and extract a user_id
    # In production, verify against Supabase Auth: https://supabase.com/docs/guides/auth
    token = credentials.credentials

    # For testing/demo, accept UUID format tokens
    try:
        user_id = uuid.UUID(token)
        return {"user_id": user_id}
    except ValueError:
        # For demo, accept any token and use it as user_id
        return {"user_id": uuid.uuid4()}

