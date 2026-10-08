from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from uuid import UUID
from decimal import Decimal


class BuildingBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    address: str
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    building_type: Optional[str] = None
    square_feet: Optional[int] = None
    annual_energy_cost: Optional[Decimal] = None
    current_utilities: dict = {}


class BuildingCreate(BuildingBase):
    client_id: UUID


class BuildingUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    building_type: Optional[str] = None
    square_feet: Optional[int] = None
    annual_energy_cost: Optional[Decimal] = None
    current_utilities: Optional[dict] = None


class BuildingResponse(BuildingBase):
    id: UUID
    consultant_id: UUID
    client_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class RecommendationBase(BaseModel):
    category: str = Field(..., min_length=1, max_length=100)
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    annual_savings: Optional[Decimal] = None
    implementation_cost: Optional[Decimal] = None
    payback_years: Optional[Decimal] = None
    priority: Optional[str] = None
    status: str = "pending"


class RecommendationCreate(RecommendationBase):
    building_id: UUID


class RecommendationUpdate(BaseModel):
    category: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    annual_savings: Optional[Decimal] = None
    implementation_cost: Optional[Decimal] = None
    payback_years: Optional[Decimal] = None
    priority: Optional[str] = None
    status: Optional[str] = None


class RecommendationResponse(RecommendationBase):
    id: UUID
    consultant_id: UUID
    building_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class AnalysisBase(BaseModel):
    current_spend: Optional[Decimal] = None
    estimated_savings: Optional[Decimal] = None
    roi_percentage: Optional[Decimal] = None
    recommendation_count: int = 0


class AnalysisCreate(AnalysisBase):
    building_id: UUID


class AnalysisUpdate(BaseModel):
    current_spend: Optional[Decimal] = None
    estimated_savings: Optional[Decimal] = None
    roi_percentage: Optional[Decimal] = None
    recommendation_count: Optional[int] = None


class AnalysisResponse(AnalysisBase):
    id: UUID
    consultant_id: UUID
    building_id: UUID
    analysis_date: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class BuildingWithAnalysis(BuildingResponse):
    recommendations: List[RecommendationResponse] = []
    analysis: Optional[AnalysisResponse] = None

    class Config:
        from_attributes = True
