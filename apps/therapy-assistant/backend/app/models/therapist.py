from sqlalchemy import Column, String, Text, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime

from app.core.database import Base


class Therapist(Base):
    __tablename__ = "therapists"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(20))
    license_number = Column(String(100))
    specialization = Column(String(255))
    bio = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    clients = relationship("Client", back_populates="therapist", cascade="all, delete-orphan")
    sessions = relationship("Session", back_populates="therapist", cascade="all, delete-orphan")
    tasks = relationship("Task", back_populates="therapist", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Therapist(id={self.id}, name={self.name}, email={self.email})>"
