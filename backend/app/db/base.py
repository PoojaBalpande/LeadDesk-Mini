from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Central Declarative Base class for all SQLAlchemy 2.x ORM models.
    
    Future models (e.g. Lead, User, Organization) will inherit from this Base class.
    """
