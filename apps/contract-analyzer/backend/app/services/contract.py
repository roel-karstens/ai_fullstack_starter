from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from typing import List, Optional

from app.models import Contract, RiskFlag, Analysis
from app.schemas import (
    ContractCreate,
    ContractUpdate,
    RiskFlagCreate,
    RiskFlagUpdate,
    AnalysisCreate,
    AnalysisUpdate,
)


class ContractService:
    """Service layer for Contract Analyzer operations."""

    @staticmethod
    async def create_contract(db: AsyncSession, contract_data: ContractCreate, lawyer_id: UUID) -> Contract:
        """Create a new contract."""
        db_contract = Contract(
            lawyer_id=lawyer_id,
            **contract_data.model_dump()
        )
        db.add(db_contract)
        await db.commit()
        await db.refresh(db_contract)
        return db_contract

    @staticmethod
    async def get_contracts(db: AsyncSession, lawyer_id: UUID) -> List[Contract]:
        """Get all contracts for a lawyer."""
        result = await db.execute(
            select(Contract).where(Contract.lawyer_id == lawyer_id)
        )
        return result.scalars().all()

    @staticmethod
    async def get_contract(db: AsyncSession, contract_id: UUID, lawyer_id: UUID) -> Optional[Contract]:
        """Get a specific contract."""
        result = await db.execute(
            select(Contract).where(
                (Contract.id == contract_id) & (Contract.lawyer_id == lawyer_id)
            )
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def update_contract(
        db: AsyncSession, contract_id: UUID, lawyer_id: UUID, contract_data: ContractUpdate
    ) -> Optional[Contract]:
        """Update a contract."""
        db_contract = await ContractService.get_contract(db, contract_id, lawyer_id)
        if not db_contract:
            return None

        update_data = contract_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_contract, field, value)

        db.add(db_contract)
        await db.commit()
        await db.refresh(db_contract)
        return db_contract

    @staticmethod
    async def delete_contract(db: AsyncSession, contract_id: UUID, lawyer_id: UUID) -> bool:
        """Delete a contract."""
        db_contract = await ContractService.get_contract(db, contract_id, lawyer_id)
        if not db_contract:
            return False

        await db.delete(db_contract)
        await db.commit()
        return True

    @staticmethod
    async def create_risk_flag(db: AsyncSession, risk_data: RiskFlagCreate, lawyer_id: UUID) -> RiskFlag:
        """Create a risk flag for a contract."""
        db_risk = RiskFlag(
            lawyer_id=lawyer_id,
            **risk_data.model_dump()
        )
        db.add(db_risk)
        await db.commit()
        await db.refresh(db_risk)
        return db_risk

    @staticmethod
    async def get_contract_risks(db: AsyncSession, contract_id: UUID, lawyer_id: UUID) -> List[RiskFlag]:
        """Get all risk flags for a contract."""
        result = await db.execute(
            select(RiskFlag).where(
                (RiskFlag.contract_id == contract_id) & (RiskFlag.lawyer_id == lawyer_id)
            )
        )
        return result.scalars().all()

    @staticmethod
    async def create_analysis(db: AsyncSession, analysis_data: AnalysisCreate, lawyer_id: UUID) -> Analysis:
        """Create analysis for a contract."""
        db_analysis = Analysis(
            lawyer_id=lawyer_id,
            **analysis_data.model_dump()
        )
        db.add(db_analysis)
        await db.commit()
        await db.refresh(db_analysis)
        return db_analysis

    @staticmethod
    async def get_analysis(db: AsyncSession, contract_id: UUID, lawyer_id: UUID) -> Optional[Analysis]:
        """Get analysis for a contract."""
        result = await db.execute(
            select(Analysis).where(
                (Analysis.contract_id == contract_id) & (Analysis.lawyer_id == lawyer_id)
            )
        )
        return result.scalar_one_or_none()
