from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime
from uuid import UUID
from decimal import Decimal


class ContractBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    file_name: str
    file_url: str
    parties: List[str] = []
    obligations: List[str] = []


class ContractCreate(ContractBase):
    pass


class ContractUpdate(BaseModel):
    title: Optional[str] = None
    parties: Optional[List[str]] = None
    obligations: Optional[List[str]] = None


class ContractResponse(ContractBase):
    id: UUID
    lawyer_id: UUID
    risk_score: int
    analysis_status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class RiskFlagBase(BaseModel):
    severity: str = Field(..., pattern="^(critical|warning|info)$")
    title: str = Field(..., min_length=1, max_length=255)
    description: str
    recommendation: Optional[str] = None


class RiskFlagCreate(RiskFlagBase):
    contract_id: UUID


class RiskFlagUpdate(BaseModel):
    severity: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    recommendation: Optional[str] = None


class RiskFlagResponse(RiskFlagBase):
    id: UUID
    contract_id: UUID
    lawyer_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class AnalysisBase(BaseModel):
    extracted_terms: dict = {}
    safe_clauses: List[str] = []
    comparison_result: dict = {}


class AnalysisCreate(AnalysisBase):
    contract_id: UUID


class AnalysisUpdate(BaseModel):
    extracted_terms: Optional[dict] = None
    safe_clauses: Optional[List[str]] = None
    comparison_result: Optional[dict] = None


class AnalysisResponse(AnalysisBase):
    id: UUID
    contract_id: UUID
    lawyer_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ContractWithAnalysis(ContractResponse):
    risk_flags: List[RiskFlagResponse] = []
    analysis: Optional[AnalysisResponse] = None

    class Config:
        from_attributes = True
