from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import LeadSource, LeadStatus

if TYPE_CHECKING:
    from app.models.user import User


class Lead(Base):
    """Lead ORM Model representing potential clients and deal opportunities."""

    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    phone: Mapped[str | None] = mapped_column(String(20), index=True, nullable=True)
    company: Mapped[str | None] = mapped_column(String(100), index=True, nullable=True)
    message: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[LeadStatus] = mapped_column(
        Enum(LeadStatus, native_enum=False),
        nullable=False,
        default=LeadStatus.NEW,
        index=True,
    )
    source: Mapped[LeadSource] = mapped_column(
        Enum(LeadSource, native_enum=False),
        nullable=False,
        default=LeadSource.OTHER,
        index=True,
    )
    assigned_user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    # Relationships
    assigned_user: Mapped[User | None] = relationship(
        "User",
        back_populates="leads",
    )
