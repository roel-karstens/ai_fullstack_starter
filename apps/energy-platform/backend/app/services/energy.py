from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from typing import List, Optional

from app.models import Building, Recommendation, Analysis
from app.schemas import (
    BuildingCreate,
    BuildingUpdate,
    RecommendationCreate,
    RecommendationUpdate,
    AnalysisCreate,
    AnalysisUpdate,
)


class EnergyService:
    """Service layer for Energy Platform operations."""

    @staticmethod
    async def create_building(db: AsyncSession, building_data: BuildingCreate, consultant_id: UUID) -> Building:
        """Create a new building."""
        db_building = Building(
            consultant_id=consultant_id,
            **building_data.model_dump()
        )
        db.add(db_building)
        await db.commit()
        await db.refresh(db_building)
        return db_building

    @staticmethod
    async def get_buildings(db: AsyncSession, consultant_id: UUID, client_id: Optional[UUID] = None) -> List[Building]:
        """Get all buildings for a consultant, optionally filtered by client."""
        if client_id:
            result = await db.execute(
                select(Building).where(
                    (Building.consultant_id == consultant_id) & (Building.client_id == client_id)
                )
            )
        else:
            result = await db.execute(
                select(Building).where(Building.consultant_id == consultant_id)
            )
        return result.scalars().all()

    @staticmethod
    async def get_building(db: AsyncSession, building_id: UUID, consultant_id: UUID) -> Optional[Building]:
        """Get a specific building."""
        result = await db.execute(
            select(Building).where(
                (Building.id == building_id) & (Building.consultant_id == consultant_id)
            )
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def update_building(
        db: AsyncSession, building_id: UUID, consultant_id: UUID, building_data: BuildingUpdate
    ) -> Optional[Building]:
        """Update a building."""
        db_building = await EnergyService.get_building(db, building_id, consultant_id)
        if not db_building:
            return None

        update_data = building_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_building, field, value)

        db.add(db_building)
        await db.commit()
        await db.refresh(db_building)
        return db_building

    @staticmethod
    async def delete_building(db: AsyncSession, building_id: UUID, consultant_id: UUID) -> bool:
        """Delete a building."""
        db_building = await EnergyService.get_building(db, building_id, consultant_id)
        if not db_building:
            return False

        await db.delete(db_building)
        await db.commit()
        return True

    @staticmethod
    async def create_recommendation(
        db: AsyncSession, rec_data: RecommendationCreate, consultant_id: UUID
    ) -> Recommendation:
        """Create a recommendation for a building."""
        db_rec = Recommendation(
            consultant_id=consultant_id,
            **rec_data.model_dump()
        )
        db.add(db_rec)
        await db.commit()
        await db.refresh(db_rec)
        return db_rec

    @staticmethod
    async def get_building_recommendations(
        db: AsyncSession, building_id: UUID, consultant_id: UUID
    ) -> List[Recommendation]:
        """Get all recommendations for a building."""
        result = await db.execute(
            select(Recommendation).where(
                (Recommendation.building_id == building_id) & (Recommendation.consultant_id == consultant_id)
            )
        )
        return result.scalars().all()

    @staticmethod
    async def create_analysis(db: AsyncSession, analysis_data: AnalysisCreate, consultant_id: UUID) -> Analysis:
        """Create analysis for a building."""
        db_analysis = Analysis(
            consultant_id=consultant_id,
            **analysis_data.model_dump()
        )
        db.add(db_analysis)
        await db.commit()
        await db.refresh(db_analysis)
        return db_analysis

    @staticmethod
    async def get_analysis(db: AsyncSession, building_id: UUID, consultant_id: UUID) -> Optional[Analysis]:
        """Get analysis for a building."""
        result = await db.execute(
            select(Analysis).where(
                (Analysis.building_id == building_id) & (Analysis.consultant_id == consultant_id)
            )
        )
        return result.scalar_one_or_none()
