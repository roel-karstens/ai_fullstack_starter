from sqlalchemy import Column, String, Text, Integer, Float, DateTime, func, ForeignKey, ARRAY, JSON, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime

from app.core.database import Base


class Building(Base):
    __tablename__ = "buildings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    consultant_id = Column(UUID(as_uuid=True), nullable=False)
    client_id = Column(UUID(as_uuid=True), nullable=False)
    name = Column(String(255), nullable=False)
    address = Column(Text, nullable=False)
    city = Column(String(255))
    state = Column(String(50))
    postal_code = Column(String(20))
    country = Column(String(255))
    building_type = Column(String(100))  # warehouse, office, retail
    square_feet = Column(Integer)
    annual_energy_cost = Column(Numeric(12, 2))
    current_utilities = Column(JSON, default={})  # gas, electric, water
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    recommendations = relationship("Recommendation", back_populates="building", cascade="all, delete-orphan")
    analysis = relationship("Analysis", back_populates="building", uselist=False, cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Building(id={self.id}, name={self.name}, address={self.address})>"


class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    consultant_id = Column(UUID(as_uuid=True), nullable=False)
    building_id = Column(UUID(as_uuid=True), ForeignKey("buildings.id"), nullable=False)
    category = Column(String(100), nullable=False)  # HVAC, Lighting, Insulation, Solar, Water
    title = Column(String(255), nullable=False)
    description = Column(Text)
    annual_savings = Column(Numeric(12, 2))
    implementation_cost = Column(Numeric(12, 2))
    payback_years = Column(Numeric(5, 2))
    priority = Column(String(50))  # High, Medium, Low
    status = Column(String(50), default="pending")  # pending, approved, implemented
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    building = relationship("Building", back_populates="recommendations")

    def __repr__(self) -> str:
        return f"<Recommendation(id={self.id}, category={self.category}, title={self.title})>"


class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    consultant_id = Column(UUID(as_uuid=True), nullable=False)
    building_id = Column(UUID(as_uuid=True), ForeignKey("buildings.id"), unique=True, nullable=False)
    current_spend = Column(Numeric(12, 2))
    estimated_savings = Column(Numeric(12, 2))
    roi_percentage = Column(Numeric(5, 2))
    recommendation_count = Column(Integer, default=0)
    analysis_date = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    building = relationship("Building", back_populates="analysis")

    def __repr__(self) -> str:
        return f"<Analysis(id={self.id}, building_id={self.building_id})>"
