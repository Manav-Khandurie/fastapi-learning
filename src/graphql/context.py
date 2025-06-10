from fastapi import Depends
from sqlalchemy.orm import Session
from strawberry.fastapi import BaseContext

from src.database.dependency import get_db
from src.utils.logger import logger


# Strawberry GraphQL Context
class Context(BaseContext):
    """
    Represents the GraphQL context that holds the database session.

    Attributes:
        db (Session): The database session used for GraphQL operations.
    """
    def __init__(self, db: Session):
        """
        Initializes the GraphQL context with a database session.

        Args:
            db (Session): The database session to be used in the context.
        """
        logger.info("📚 Initializing GraphQL context with DB session")
        self.db = db


async def get_context(db: Session = Depends(get_db)):
    """
    Dependency that provides the GraphQL context with a database session.

    Args:
        db (Session, optional): The database session, automatically provided by FastAPI's dependency injection.

    Returns:
        Context: An instance of the Context class containing the database session.
    """
    logger.info("🔗 Creating GraphQL context dependency")
    return Context(db=db)