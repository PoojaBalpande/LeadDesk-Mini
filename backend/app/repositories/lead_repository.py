from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from app.models.enums import LeadSource, LeadStatus
from app.models.lead import Lead


class LeadRepository:
    """Repository handling database persistence operations for the Lead entity."""

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_id(self, lead_id: int) -> Lead | None:
        """Fetch a Lead by primary key ID."""
        return self.db.get(Lead, lead_id)

    def create(self, lead: Lead) -> Lead:
        """Persist a new Lead entity in the database."""
        self.db.add(lead)
        self.db.commit()
        self.db.refresh(lead)
        return lead

    def update(self, lead: Lead) -> Lead:
        """Update an existing Lead entity in the database."""
        self.db.commit()
        self.db.refresh(lead)
        return lead

    def delete(self, lead: Lead) -> bool:
        """Remove a Lead entity from the database."""
        self.db.delete(lead)
        self.db.commit()
        return True

    def list_leads(self, skip: int = 0, limit: int = 100) -> list[Lead]:
        """Retrieve a paginated list of leads."""
        stmt = select(Lead).offset(skip).limit(limit)
        return list(self.db.scalars(stmt).all())

    def search(self, query_str: str, skip: int = 0, limit: int = 100) -> list[Lead]:
        """Search leads by matching name, email, company, or message."""
        pattern = f"%{query_str}%"
        stmt = (
            select(Lead)
            .where(
                or_(
                    Lead.name.ilike(pattern),
                    Lead.email.ilike(pattern),
                    Lead.company.ilike(pattern),
                    Lead.message.ilike(pattern),
                )
            )
            .offset(skip)
            .limit(limit)
        )
        return list(self.db.scalars(stmt).all())

    def filter_by_status(self, status: LeadStatus, skip: int = 0, limit: int = 100) -> list[Lead]:
        """Filter leads by lifecycle status."""
        stmt = select(Lead).where(Lead.status == status).offset(skip).limit(limit)
        return list(self.db.scalars(stmt).all())

    def filter_by_source(self, source: LeadSource, skip: int = 0, limit: int = 100) -> list[Lead]:
        """Filter leads by acquisition source."""
        stmt = select(Lead).where(Lead.source == source).offset(skip).limit(limit)
        return list(self.db.scalars(stmt).all())

    def filter_by_assigned_user(self, user_id: int, skip: int = 0, limit: int = 100) -> list[Lead]:
        """Filter leads assigned to a specific user."""
        stmt = select(Lead).where(Lead.assigned_user_id == user_id).offset(skip).limit(limit)
        return list(self.db.scalars(stmt).all())

    def count_by_status(self, status: LeadStatus) -> int:
        """Count the total number of leads with a given status."""
        stmt = select(func.count()).select_from(Lead).where(Lead.status == status)
        count = self.db.scalar(stmt)
        return count if count is not None else 0

    def recent_leads(self, limit: int = 10) -> list[Lead]:
        """Fetch the most recently created leads ordered by creation timestamp."""
        stmt = select(Lead).order_by(Lead.created_at.desc()).limit(limit)
        return list(self.db.scalars(stmt).all())
