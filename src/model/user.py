from sqlalchemy import Column, Integer, String

from src.database.base import Base


class User(Base):
    """Represents a user in the system."""
    
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # User's name, cannot be null.