from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List, Optional

from app.dependencies import get_db, get_current_user
from app.services.energy import EnergyService
from app.schemas import (
    BuildingCreate,
    BuildingUpdate,
    BuildingResponse,
    BuildingWithAnalysis,
    RecommendationCreate,
    RecommendationUpdate,
    RecommendationResponse,
    AnalysisCreate,
    AnalysisResponse,
)

router = APIRouter(prefix="/api/v1/buildings", tags=["buildings"])


@router.post("", response_model=BuildingResponse, status_code=status.HTTP_201_CREATED)
async def create_building(
    building: BuildingCreate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Create a new building."""
    db_building = await EnergyService.create_building(db, building, current_user["user_id"])
    return db_building


@router.get("", response_model=List[BuildingResponse])
async def list_buildings(
    client_id: Optional[UUID] = Query(None),
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """List all buildings for current user, optionally filtered by client."""
    buildings = await EnergyService.get_buildings(db, current_user["user_id"], client_id)
    return buildings


@router.get("/{building_id}", response_model=BuildingWithAnalysis)
async def get_building(
    building_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Get a specific building with analysis and recommendations."""
    db_building = await EnergyService.get_building(db, building_id, current_user["user_id"])
    if not db_building:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Building not found")
    return db_building


@router.patch("/{building_id}", response_model=BuildingResponse)
async def update_building(
    building_id: UUID,
    building: BuildingUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Update a building."""
    db_building = await EnergyService.update_building(db, building_id, current_user["user_id"], building)
    if not db_building:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Building not found")
    return db_building


@router.delete("/{building_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_building(
    building_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Delete a building."""
    success = await EnergyService.delete_building(db, building_id, current_user["user_id"])
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Building not found")


@router.post("/{building_id}/recommendations", response_model=RecommendationResponse, status_code=status.HTTP_201_CREATED)
async def create_recommendation(
    building_id: UUID,
    recommendation: RecommendationCreate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Create a recommendation for a building."""
    # Verify building exists
    db_building = await EnergyService.get_building(db, building_id, current_user["user_id"])
    if not db_building:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Building not found")

    db_rec = await EnergyService.create_recommendation(db, recommendation, current_user["user_id"])
    return db_rec


@router.get("/{building_id}/recommendations", response_model=List[RecommendationResponse])
async def get_building_recommendations(
    building_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Get all recommendations for a building."""
    # Verify building exists
    db_building = await EnergyService.get_building(db, building_id, current_user["user_id"])
    if not db_building:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Building not found")

    recommendations = await EnergyService.get_building_recommendations(db, building_id, current_user["user_id"])
    return recommendations


@router.post("/{building_id}/analysis", response_model=AnalysisResponse, status_code=status.HTTP_201_CREATED)
async def create_analysis(
    building_id: UUID,
    analysis: AnalysisCreate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Create analysis for a building."""
    # Verify building exists
    db_building = await EnergyService.get_building(db, building_id, current_user["user_id"])
    if not db_building:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Building not found")

    db_analysis = await EnergyService.create_analysis(db, analysis, current_user["user_id"])
    return db_analysis


@router.get("/{building_id}/analysis", response_model=AnalysisResponse)
async def get_analysis(
    building_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Get analysis for a building."""
    # Verify building exists
    db_building = await EnergyService.get_building(db, building_id, current_user["user_id"])
    if not db_building:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Building not found")

    analysis = await EnergyService.get_analysis(db, building_id, current_user["user_id"])
    if not analysis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Analysis not found")
    return analysis
