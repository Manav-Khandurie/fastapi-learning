import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config.config import settings
from src.utils.logger import logger

# Define the database URL from the settings configuration
SQLALCHEMY_DATABASE_URL = settings.database_url

# Create a directory named 'data' if it does not already exist
os.makedirs("data", exist_ok=True)
logger.info("📁 Ensured 'data' directory exists")

try:
    # Create a new SQLAlchemy engine instance for the database
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    logger.info(f"🗄️ Database engine created for URL: {SQLALCHEMY_DATABASE_URL}")
except Exception as e:
    # Log an error if the engine creation fails
    logger.error(f"❌ Failed to create database engine: {e}")
    raise

# Create a configured "Session" class for database interactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
logger.info("🔧 SessionLocal configured")
