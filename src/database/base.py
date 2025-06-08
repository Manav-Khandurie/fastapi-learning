from sqlalchemy.orm import declarative_base

from src.utils.logger import logger

# Initialize the SQLAlchemy declarative base for ORM mapping
Base = declarative_base()
logger.info("⚙️ SQLAlchemy declarative base initialized")