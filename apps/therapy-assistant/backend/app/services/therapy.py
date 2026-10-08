from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from typing import List, Optional

from app.models import Therapist, Client, Session, Task, MoodTracking, AISummary
from app.schemas import (
    TherapistCreate,
    TherapistUpdate,
    ClientCreate,
    ClientUpdate,
    SessionCreate,
    SessionUpdate,
    TaskCreate,
    TaskUpdate,
    MoodTrackingCreate,
    MoodTrackingUpdate,
    AISummaryCreate,
)


class TherapyService:
    """Service layer for Therapy Assistant operations."""

    @staticmethod
    async def create_therapist(db: AsyncSession, therapist_data: TherapistCreate, user_id: UUID) -> Therapist:
        """Create a new therapist profile."""
        db_therapist = Therapist(
            id=user_id,
            **therapist_data.model_dump()
        )
        db.add(db_therapist)
        await db.commit()
        await db.refresh(db_therapist)
        return db_therapist

    @staticmethod
    async def get_therapist(db: AsyncSession, therapist_id: UUID) -> Optional[Therapist]:
        """Get therapist by ID."""
        result = await db.execute(select(Therapist).where(Therapist.id == therapist_id))
        return result.scalars().first()

    @staticmethod
    async def update_therapist(db: AsyncSession, therapist_id: UUID, therapist_data: TherapistUpdate) -> Optional[Therapist]:
        """Update therapist profile."""
        db_therapist = await TherapyService.get_therapist(db, therapist_id)
        if db_therapist:
            update_data = therapist_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_therapist, key, value)
            await db.commit()
            await db.refresh(db_therapist)
        return db_therapist

    # Client operations
    @staticmethod
    async def create_client(db: AsyncSession, therapist_id: UUID, client_data: ClientCreate) -> Client:
        """Create a new client."""
        db_client = Client(
            therapist_id=therapist_id,
            **client_data.model_dump()
        )
        db.add(db_client)
        await db.commit()
        await db.refresh(db_client)
        return db_client

    @staticmethod
    async def get_clients(db: AsyncSession, therapist_id: UUID) -> List[Client]:
        """Get all clients for a therapist."""
        result = await db.execute(
            select(Client).where(Client.therapist_id == therapist_id)
        )
        return result.scalars().all()

    @staticmethod
    async def get_client(db: AsyncSession, client_id: UUID, therapist_id: UUID) -> Optional[Client]:
        """Get a specific client (with authorization check)."""
        result = await db.execute(
            select(Client).where(
                (Client.id == client_id) & (Client.therapist_id == therapist_id)
            )
        )
        return result.scalars().first()

    @staticmethod
    async def update_client(db: AsyncSession, client_id: UUID, therapist_id: UUID, client_data: ClientUpdate) -> Optional[Client]:
        """Update client information."""
        db_client = await TherapyService.get_client(db, client_id, therapist_id)
        if db_client:
            update_data = client_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_client, key, value)
            await db.commit()
            await db.refresh(db_client)
        return db_client

    # Session operations
    @staticmethod
    async def create_session(db: AsyncSession, therapist_id: UUID, session_data: SessionCreate) -> Session:
        """Create a new session."""
        db_session = Session(
            therapist_id=therapist_id,
            **session_data.model_dump()
        )
        db.add(db_session)
        await db.commit()
        await db.refresh(db_session)
        return db_session

    @staticmethod
    async def get_sessions(db: AsyncSession, therapist_id: UUID, client_id: Optional[UUID] = None) -> List[Session]:
        """Get sessions for a therapist (optionally filtered by client)."""
        query = select(Session).where(Session.therapist_id == therapist_id)
        if client_id:
            query = query.where(Session.client_id == client_id)
        result = await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def get_session(db: AsyncSession, session_id: UUID, therapist_id: UUID) -> Optional[Session]:
        """Get a specific session (with authorization check)."""
        result = await db.execute(
            select(Session).where(
                (Session.id == session_id) & (Session.therapist_id == therapist_id)
            )
        )
        return result.scalars().first()

    @staticmethod
    async def update_session(db: AsyncSession, session_id: UUID, therapist_id: UUID, session_data: SessionUpdate) -> Optional[Session]:
        """Update session information."""
        db_session = await TherapyService.get_session(db, session_id, therapist_id)
        if db_session:
            update_data = session_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_session, key, value)
            await db.commit()
            await db.refresh(db_session)
        return db_session

    # Task operations
    @staticmethod
    async def create_task(db: AsyncSession, therapist_id: UUID, task_data: TaskCreate) -> Task:
        """Create a new task."""
        db_task = Task(
            therapist_id=therapist_id,
            **task_data.model_dump()
        )
        db.add(db_task)
        await db.commit()
        await db.refresh(db_task)
        return db_task

    @staticmethod
    async def get_tasks(db: AsyncSession, therapist_id: UUID, client_id: Optional[UUID] = None) -> List[Task]:
        """Get tasks for a therapist (optionally filtered by client)."""
        query = select(Task).where(Task.therapist_id == therapist_id)
        if client_id:
            query = query.where(Task.client_id == client_id)
        result = await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def update_task(db: AsyncSession, task_id: UUID, therapist_id: UUID, task_data: TaskUpdate) -> Optional[Task]:
        """Update task information."""
        result = await db.execute(
            select(Task).where((Task.id == task_id) & (Task.therapist_id == therapist_id))
        )
        db_task = result.scalars().first()
        if db_task:
            update_data = task_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_task, key, value)
            await db.commit()
            await db.refresh(db_task)
        return db_task

    # Mood tracking operations
    @staticmethod
    async def create_mood_tracking(db: AsyncSession, mood_data: MoodTrackingCreate) -> MoodTracking:
        """Create mood tracking entry."""
        db_mood = MoodTracking(**mood_data.model_dump())
        db.add(db_mood)
        await db.commit()
        await db.refresh(db_mood)
        return db_mood

    @staticmethod
    async def get_client_mood_tracking(db: AsyncSession, client_id: UUID) -> List[MoodTracking]:
        """Get mood tracking for a client."""
        result = await db.execute(
            select(MoodTracking)
            .where(MoodTracking.client_id == client_id)
            .order_by(MoodTracking.tracked_date.desc())
        )
        return result.scalars().all()

    # AI Summary operations
    @staticmethod
    async def create_ai_summary(db: AsyncSession, session_id: UUID, summary_data: AISummaryCreate) -> AISummary:
        """Create AI summary for a session."""
        db_summary = AISummary(
            session_id=session_id,
            **summary_data.model_dump()
        )
        db.add(db_summary)
        await db.commit()
        await db.refresh(db_summary)
        return db_summary

    @staticmethod
    async def get_session_summary(db: AsyncSession, session_id: UUID) -> Optional[AISummary]:
        """Get AI summary for a session."""
        result = await db.execute(
            select(AISummary).where(AISummary.session_id == session_id)
        )
        return result.scalars().first()
