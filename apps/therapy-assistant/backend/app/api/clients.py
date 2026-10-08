from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List

from app.core.database import get_db
from app.schemas import (
    ClientCreate,
    ClientUpdate,
    ClientResponse,
)
from app.services.therapy import TherapyService

router = APIRouter(prefix="/api/v1/clients", tags=["clients"])


@router.post("", response_model=ClientResponse, status_code=status.HTTP_201_CREATED)
async def create_client(
    client_data: ClientCreate,
    current_user_id: UUID = Depends(lambda: UUID("00000000-0000-0000-0000-000000000000")),  # TODO: Add auth
    db: AsyncSession = Depends(get_db),
) -> ClientResponse:
    """Create a new client."""
    return await TherapyService.create_client(db, current_user_id, client_data)


@router.get("", response_model=List[ClientResponse])
async def list_clients(
    current_user_id: UUID = Depends(lambda: UUID("00000000-0000-0000-0000-000000000000")),  # TODO: Add auth
    db: AsyncSession = Depends(get_db),
) -> List[ClientResponse]:
    """List all clients for the current therapist."""
    return await TherapyService.get_clients(db, current_user_id)


@router.get("/{client_id}", response_model=ClientResponse)
async def get_client(
    client_id: UUID,
    current_user_id: UUID = Depends(lambda: UUID("00000000-0000-0000-0000-000000000000")),  # TODO: Add auth
    db: AsyncSession = Depends(get_db),
) -> ClientResponse:
    """Get a specific client."""
    client = await TherapyService.get_client(db, client_id, current_user_id)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
    return client


@router.patch("/{client_id}", response_model=ClientResponse)
async def update_client(
    client_id: UUID,
    client_data: ClientUpdate,
    current_user_id: UUID = Depends(lambda: UUID("00000000-0000-0000-0000-000000000000")),  # TODO: Add auth
    db: AsyncSession = Depends(get_db),
) -> ClientResponse:
    """Update a client."""
    client = await TherapyService.update_client(db, client_id, current_user_id, client_data)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
    return client


@router.delete("/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_client(
    client_id: UUID,
    current_user_id: UUID = Depends(lambda: UUID("00000000-0000-0000-0000-000000000000")),  # TODO: Add auth
    db: AsyncSession = Depends(get_db),
) -> None:
    """Delete a client."""
    client = await TherapyService.get_client(db, client_id, current_user_id)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
    await db.delete(client)
    await db.commit()
