from collections.abc import Generator

from sqlalchemy.orm import Session

from src.database.database import SessionLocal
from src.utils.logger import logger


def get_db() -> Generator[Session, None, None]:
    """Create a new database session and yield it.

    This function initializes a new database session using the SessionLocal
    factory and ensures that the session is properly closed after use.

    Yields:
        Generator[Session, None, None]: A generator that yields a database session.
    """
    logger.info("🔗 Creating new DB session")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # Ensure the database session is closed
        logger.info("🔒 DB session closed")