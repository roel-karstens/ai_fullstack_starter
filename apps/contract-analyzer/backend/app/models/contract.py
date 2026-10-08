from sqlalchemy import Column, String, Text, Integer, DateTime, func, ForeignKey, ARRAY, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime

from app.core.database import Base


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lawyer_id = Column(UUID(as_uuid=True), nullable=False)
    title = Column(String(255), nullable=False)
    file_name = Column(String(255), nullable=False)
    file_url = Column(Text, nullable=False)
    parties = Column(ARRAY(String), default=[])
    key_dates = Column(JSON, default={})
    obligations = Column(ARRAY(String), default=[])
    risk_score = Column(Integer, default=0)
    analysis_status = Column(String(50), default="pending")  # pending, analyzing, completed
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    risk_flags = relationship("RiskFlag", back_populates="contract", cascade="all, delete-orphan")
    analysis = relationship("Analysis", back_populates="contract", uselist=False, cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Contract(id={self.id}, title={self.title}, risk_score={self.risk_score})>"


class RiskFlag(Base):
    __tablename__ = "risk_flags"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    contract_id = Column(UUID(as_uuid=True), ForeignKey("contracts.id"), nullable=False)
    lawyer_id = Column(UUID(as_uuid=True), nullable=False)
    severity = Column(String(50), nullable=False)  # critical, warning, info
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    recommendation = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    contract = relationship("Contract", back_populates="risk_flags")

    def __repr__(self) -> str:
        return f"<RiskFlag(id={self.id}, severity={self.severity}, title={self.title})>"


class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    contract_id = Column(UUID(as_uuid=True), ForeignKey("contracts.id"), unique=True, nullable=False)
    lawyer_id = Column(UUID(as_uuid=True), nullable=False)
    extracted_terms = Column(JSON, default={})
    safe_clauses = Column(ARRAY(String), default=[])
    comparison_result = Column(JSON, default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    contract = relationship("Contract", back_populates="analysis")

    def __repr__(self) -> str:
        return f"<Analysis(id={self.id}, contract_id={self.contract_id})>"
