from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List

from app.dependencies import get_db, get_current_user
from app.services.contract import ContractService
from app.schemas import (
    ContractCreate,
    ContractUpdate,
    ContractResponse,
    ContractWithAnalysis,
    RiskFlagCreate,
    RiskFlagResponse,
    AnalysisCreate,
    AnalysisResponse,
)

router = APIRouter(prefix="/api/v1/contracts", tags=["contracts"])


@router.post("", response_model=ContractResponse, status_code=status.HTTP_201_CREATED)
async def create_contract(
    contract: ContractCreate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Create a new contract."""
    db_contract = await ContractService.create_contract(db, contract, current_user["user_id"])
    return db_contract


@router.get("", response_model=List[ContractResponse])
async def list_contracts(
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """List all contracts for current user."""
    contracts = await ContractService.get_contracts(db, current_user["user_id"])
    return contracts


@router.get("/{contract_id}", response_model=ContractWithAnalysis)
async def get_contract(
    contract_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Get a specific contract with analysis and risks."""
    db_contract = await ContractService.get_contract(db, contract_id, current_user["user_id"])
    if not db_contract:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contract not found")
    return db_contract


@router.patch("/{contract_id}", response_model=ContractResponse)
async def update_contract(
    contract_id: UUID,
    contract: ContractUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Update a contract."""
    db_contract = await ContractService.update_contract(db, contract_id, current_user["user_id"], contract)
    if not db_contract:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contract not found")
    return db_contract


@router.delete("/{contract_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contract(
    contract_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Delete a contract."""
    success = await ContractService.delete_contract(db, contract_id, current_user["user_id"])
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contract not found")


@router.post("/{contract_id}/risks", response_model=RiskFlagResponse, status_code=status.HTTP_201_CREATED)
async def create_risk_flag(
    contract_id: UUID,
    risk_flag: RiskFlagCreate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Create a risk flag for a contract."""
    # Verify contract exists and belongs to user
    db_contract = await ContractService.get_contract(db, contract_id, current_user["user_id"])
    if not db_contract:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contract not found")

    db_risk = await ContractService.create_risk_flag(db, risk_flag, current_user["user_id"])
    return db_risk


@router.get("/{contract_id}/risks", response_model=List[RiskFlagResponse])
async def get_contract_risks(
    contract_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Get all risk flags for a contract."""
    # Verify contract exists
    db_contract = await ContractService.get_contract(db, contract_id, current_user["user_id"])
    if not db_contract:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contract not found")

    risks = await ContractService.get_contract_risks(db, contract_id, current_user["user_id"])
    return risks


@router.post("/{contract_id}/analysis", response_model=AnalysisResponse, status_code=status.HTTP_201_CREATED)
async def create_analysis(
    contract_id: UUID,
    analysis: AnalysisCreate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Create analysis for a contract."""
    # Verify contract exists
    db_contract = await ContractService.get_contract(db, contract_id, current_user["user_id"])
    if not db_contract:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contract not found")

    db_analysis = await ContractService.create_analysis(db, analysis, current_user["user_id"])
    return db_analysis


@router.get("/{contract_id}/analysis", response_model=AnalysisResponse)
async def get_analysis(
    contract_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Get analysis for a contract."""
    # Verify contract exists
    db_contract = await ContractService.get_contract(db, contract_id, current_user["user_id"])
    if not db_contract:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contract not found")

    analysis = await ContractService.get_analysis(db, contract_id, current_user["user_id"])
    if not analysis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Analysis not found")
    return analysis
