from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime
from uuid import UUID


class TherapistBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    email: EmailStr
    phone: Optional[str] = None
    license_number: Optional[str] = None
    specialization: Optional[str] = None
    bio: Optional[str] = None


class TherapistCreate(TherapistBase):
    pass


class TherapistUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    license_number: Optional[str] = None
    specialization: Optional[str] = None
    bio: Optional[str] = None


class TherapistResponse(TherapistBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ClientBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    email: Optional[str] = None
    phone: Optional[str] = None
    date_of_birth: Optional[str] = None
    presenting_issues: Optional[str] = None
    notes: Optional[str] = None
    status: Optional[str] = Field("active", regex="^(active|inactive|discharged)$")


class ClientCreate(ClientBase):
    pass


class ClientUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    date_of_birth: Optional[str] = None
    presenting_issues: Optional[str] = None
    notes: Optional[str] = None
    status: Optional[str] = None


class ClientResponse(ClientBase):
    id: UUID
    therapist_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class SessionBase(BaseModel):
    client_id: UUID
    session_date: datetime
    duration_minutes: Optional[int] = None
    notes: Optional[str] = None
    mood_before: Optional[int] = Field(None, ge=1, le=10)
    mood_after: Optional[int] = Field(None, ge=1, le=10)


class SessionCreate(SessionBase):
    pass


class SessionUpdate(BaseModel):
    session_date: Optional[datetime] = None
    duration_minutes: Optional[int] = None
    notes: Optional[str] = None
    mood_before: Optional[int] = Field(None, ge=1, le=10)
    mood_after: Optional[int] = Field(None, ge=1, le=10)


class SessionResponse(SessionBase):
    id: UUID
    therapist_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class AISummaryCreate(BaseModel):
    summary: Optional[str] = None
    key_topics: Optional[List[str]] = []
    goals: Optional[List[str]] = []
    action_items: Optional[List[str]] = []
    recommended_focus: Optional[str] = None


class AISummaryResponse(AISummaryCreate):
    id: UUID
    session_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TaskBase(BaseModel):
    client_id: UUID
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    due_date: Optional[str] = None
    status: Optional[str] = Field("pending", regex="^(pending|completed|skipped)$")


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[str] = None
    status: Optional[str] = None


class TaskResponse(TaskBase):
    id: UUID
    therapist_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class MoodTrackingBase(BaseModel):
    client_id: UUID
    mood_score: Optional[int] = Field(None, ge=1, le=10)
    anxiety_score: Optional[int] = Field(None, ge=1, le=10)
    sleep_quality: Optional[int] = Field(None, ge=1, le=10)
    stress_level: Optional[int] = Field(None, ge=1, le=10)
    notes: Optional[str] = None
    tracked_date: str


class MoodTrackingCreate(MoodTrackingBase):
    pass


class MoodTrackingUpdate(BaseModel):
    mood_score: Optional[int] = Field(None, ge=1, le=10)
    anxiety_score: Optional[int] = Field(None, ge=1, le=10)
    sleep_quality: Optional[int] = Field(None, ge=1, le=10)
    stress_level: Optional[int] = Field(None, ge=1, le=10)
    notes: Optional[str] = None
    tracked_date: Optional[str] = None


class MoodTrackingResponse(MoodTrackingBase):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
