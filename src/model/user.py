from sqlalchemy import Column, Integer, String

from src.database.base import Base


class User(Base):
    """Represents a user in the system.

    Attributes:
        id (int): The unique identifier for the user.
        name (str): The name of the user.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for the user
    name = Column(String, nullable=False)  # Name of the user, cannot be null