from sqlalchemy import Column, String, Text, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import relationship
import uuid

from app.core.database import Base


class AISummary(Base):
    __tablename__ = "ai_summaries"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(UUID(as_uuid=True), ForeignKey("sessions.id", ondelete="CASCADE"), unique=True, nullable=False)
    summary = Column(Text)
    key_topics = Column(ARRAY(String), default=[])
    goals = Column(ARRAY(String), default=[])
    action_items = Column(ARRAY(String), default=[])
    recommended_focus = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    session = relationship("Session", back_populates="ai_summary")

    def __repr__(self) -> str:
        return f"<AISummary(id={self.id}, session_id={self.session_id})>"
