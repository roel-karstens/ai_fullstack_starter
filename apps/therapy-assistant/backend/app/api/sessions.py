from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List, Optional

from app.core.database import get_db
from app.schemas import (
    SessionCreate,
    SessionUpdate,
    SessionResponse,
    AISummaryCreate,
    AISummaryResponse,
)
from app.services.therapy import TherapyService

router = APIRouter(prefix="/api/v1/sessions", tags=["sessions"])


@router.post("", response_model=SessionResponse, status_code=status.HTTP_201_CREATED)
async def create_session(
    session_data: SessionCreate,
    current_user_id: UUID = Depends(lambda: UUID("00000000-0000-0000-0000-000000000000")),  # TODO: Add auth
    db: AsyncSession = Depends(get_db),
) -> SessionResponse:
    """Create a new session."""
    return await TherapyService.create_session(db, current_user_id, session_data)


@router.get("", response_model=List[SessionResponse])
async def list_sessions(
    client_id: Optional[UUID] = Query(None),
    current_user_id: UUID = Depends(lambda: UUID("00000000-0000-0000-0000-000000000000")),  # TODO: Add auth
    db: AsyncSession = Depends(get_db),
) -> List[SessionResponse]:
    """List all sessions for the current therapist (optionally filtered by client)."""
    return await TherapyService.get_sessions(db, current_user_id, client_id)


@router.get("/{session_id}", response_model=SessionResponse)
async def get_session(
    session_id: UUID,
    current_user_id: UUID = Depends(lambda: UUID("00000000-0000-0000-0000-000000000000")),  # TODO: Add auth
    db: AsyncSession = Depends(get_db),
) -> SessionResponse:
    """Get a specific session."""
    session = await TherapyService.get_session(db, session_id, current_user_id)
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
    return session


@router.patch("/{session_id}", response_model=SessionResponse)
async def update_session(
    session_id: UUID,
    session_data: SessionUpdate,
    current_user_id: UUID = Depends(lambda: UUID("00000000-0000-0000-0000-000000000000")),  # TODO: Add auth
    db: AsyncSession = Depends(get_db),
) -> SessionResponse:
    """Update a session."""
    session = await TherapyService.update_session(db, session_id, current_user_id, session_data)
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
    return session


@router.post("/{session_id}/summary", response_model=AISummaryResponse, status_code=status.HTTP_201_CREATED)
async def create_session_summary(
    session_id: UUID,
    summary_data: AISummaryCreate,
    current_user_id: UUID = Depends(lambda: UUID("00000000-0000-0000-0000-000000000000")),  # TODO: Add auth
    db: AsyncSession = Depends(get_db),
) -> AISummaryResponse:
    """Create AI summary for a session."""
    session = await TherapyService.get_session(db, session_id, current_user_id)
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
    return await TherapyService.create_ai_summary(db, session_id, summary_data)


@router.get("/{session_id}/summary", response_model=AISummaryResponse)
async def get_session_summary(
    session_id: UUID,
    current_user_id: UUID = Depends(lambda: UUID("00000000-0000-0000-0000-000000000000")),  # TODO: Add auth
    db: AsyncSession = Depends(get_db),
) -> AISummaryResponse:
    """Get AI summary for a session."""
    session = await TherapyService.get_session(db, session_id, current_user_id)
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
    summary = await TherapyService.get_session_summary(db, session_id)
    if not summary:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Summary not found")
    return summary
