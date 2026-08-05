from app.exceptions.repository import EntityNotFoundError
from app.exceptions.service import ValidationError
from app.models.enums import LeadStatus
from app.models.lead import Lead
from app.repositories.lead_repository import LeadRepository
from app.repositories.user_repository import UserRepository
from app.schemas.lead import LeadCreate, LeadUpdate


class LeadService:
    """Service executing business rules, lead lifecycle management, and user assignment."""

    def __init__(
        self,
        lead_repository: LeadRepository,
        user_repository: UserRepository | None = None,
    ) -> None:
        self.lead_repository = lead_repository
        self.user_repository = user_repository

    def create_lead(self, lead_create: LeadCreate) -> Lead:
        """Create and persist a new lead after validating assigned user and business rules."""
        if lead_create.assigned_user_id is not None and self.user_repository and not self.user_repository.get_by_id(lead_create.assigned_user_id):
            raise EntityNotFoundError("User", lead_create.assigned_user_id)

        lead = Lead(
            name=lead_create.name,
            email=lead_create.email,
            phone=lead_create.phone,
            company=lead_create.company,
            message=lead_create.message,
            status=lead_create.status,
            source=lead_create.source,
            assigned_user_id=lead_create.assigned_user_id,
        )
        return self.lead_repository.create(lead)

    def update_lead(self, lead_id: int, lead_update: LeadUpdate) -> Lead:
        """Update an existing lead with partial field updates."""
        lead = self.lead_repository.get_by_id(lead_id)
        if not lead:
            raise EntityNotFoundError("Lead", lead_id)

        update_data = lead_update.model_dump(exclude_unset=True)

        if "assigned_user_id" in update_data and update_data["assigned_user_id"] is not None:
            user_id = update_data["assigned_user_id"]
            if self.user_repository and not self.user_repository.get_by_id(user_id):
                raise EntityNotFoundError("User", user_id)

        for field, value in update_data.items():
            setattr(lead, field, value)

        return self.lead_repository.update(lead)

    def assign_user(self, lead_id: int, user_id: int | None) -> Lead:
        """Assign or reassign a lead to a sales team member."""
        lead = self.lead_repository.get_by_id(lead_id)
        if not lead:
            raise EntityNotFoundError("Lead", lead_id)

        if user_id is not None and self.user_repository and not self.user_repository.get_by_id(user_id):
            raise EntityNotFoundError("User", user_id)

        lead.assigned_user_id = user_id
        return self.lead_repository.update(lead)

    def change_status(self, lead_id: int, new_status: LeadStatus) -> Lead:
        """Transition a lead's lifecycle status."""
        lead = self.lead_repository.get_by_id(lead_id)
        if not lead:
            raise EntityNotFoundError("Lead", lead_id)

        lead.status = new_status
        return self.lead_repository.update(lead)

    def search_leads(self, query_str: str, skip: int = 0, limit: int = 100) -> list[Lead]:
        """Search leads by keyword after stripping surrounding whitespace."""
        clean_query = query_str.strip()
        if not clean_query:
            raise ValidationError("Search query string cannot be empty.")
        return self.lead_repository.search(clean_query, skip=skip, limit=limit)

    def validate_duplicate_lead(self, email: str) -> bool:
        """Check if a lead with the given email address already exists (True if unique)."""
        existing = self.lead_repository.search(email)
        matching = [l for l in existing if l.email.lower() == email.lower()]
        return len(matching) == 0
