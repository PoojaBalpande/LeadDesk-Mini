from enum import Enum


class UserRole(str, Enum):
    """Enumeration representing user roles for authorization and access control."""
    ADMIN = "ADMIN"
    SALES = "SALES"
    MANAGER = "MANAGER"


class LeadStatus(str, Enum):
    """Enumeration representing lifecycle status of a lead."""
    NEW = "NEW"
    CONTACTED = "CONTACTED"
    QUALIFIED = "QUALIFIED"
    PROPOSAL_SENT = "PROPOSAL_SENT"
    WON = "WON"
    LOST = "LOST"


class LeadSource(str, Enum):
    """Enumeration representing the acquisition source of a lead."""
    WEBSITE = "WEBSITE"
    EMAIL = "EMAIL"
    REFERRAL = "REFERRAL"
    SOCIAL_MEDIA = "SOCIAL_MEDIA"
    ADVERTISEMENT = "ADVERTISEMENT"
    OTHER = "OTHER"
