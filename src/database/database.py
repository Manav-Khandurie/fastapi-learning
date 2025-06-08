import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config.config import settings
from src.utils.logger import logger

SQLALCHEMY_DATABASE_URL = settings.database_url

# Create 'data' directory if it doesn't exist
os.makedirs("data", exist_ok=True)
logger.info("📁 Ensured 'data' directory exists")

try:
    # Create a new SQLAlchemy engine instance
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    logger.info(f"🗄️ Database engine created for URL: {SQLALCHEMY_DATABASE_URL}")
except Exception as e:
    logger.error(f"❌ Failed to create database engine: {e}")
    raise

# Configure a session factory for database interactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
logger.info("🔧 SessionLocal configured")