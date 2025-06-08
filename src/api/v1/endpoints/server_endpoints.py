import os

from fastapi import APIRouter

from src.utils.logger import logger

router = APIRouter()


@router.get("/health")
def get_health() -> dict:
    """Health check endpoint that returns a status message."""
    logger.info("Health check endpoint called")
    return {"message": "Healthy"}


@router.get("/env")
def get_env() -> dict:
    """Endpoint that returns the current environment variables."""
    logger.info("Environment variables requested")
    env_vars = dict(os.environ)  # Convert environment variables to a dictionary
    return env_vars


@router.get("/{full_path:path}")
def get_default_msg(full_path: str) -> dict:
    """Endpoint that handles requests to undefined paths, returning a default message."""
    logger.warning(f"Default path hit: /{full_path}")
    return {"message": f"DEFAULT PATH HIT for /{full_path}"}