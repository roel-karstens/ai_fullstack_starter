from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.core.database import Base


class MoodTracking(Base):
    __tablename__ = "mood_tracking"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    client_id = Column(UUID(as_uuid=True), ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    mood_score = Column(Integer)
    anxiety_score = Column(Integer)
    sleep_quality = Column(Integer)
    stress_level = Column(Integer)
    notes = Column(String(500))
    tracked_date = Column(String(20), nullable=False)  # DATE as string
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    client = relationship("Client", back_populates="mood_tracking")

    def __repr__(self) -> str:
        return f"<MoodTracking(id={self.id}, client_id={self.client_id}, tracked_date={self.tracked_date})>"
