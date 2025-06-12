from fastapi import APIRouter

from src.utils.logger import logger

router = APIRouter()


@router.get("/health")
def get_health() -> dict:
    """Health check endpoint that returns a status message.

    Returns:
        dict: A dictionary containing a health status message.
    """
    logger.info("Health check endpoint called")
    return {"message": "Healthy"}


# @router.get("/env")
# def get_env() -> dict:
#     """Endpoint to retrieve environment variables.

#     Returns:
#         dict: A dictionary containing the current environment variables.
#     """
#     logger.info("Environment variables requested")
#     env_vars = dict(os.environ)
#     return env_vars


@router.get("/{full_path:path}")
def get_default_msg(full_path: str) -> dict:
    """Default endpoint that returns a message for any unmatched path.

    Args:
        full_path (str): The path that was requested.

    Returns:
        dict: A dictionary containing a default message indicating the path hit.
    """
    logger.warning(f"Default path hit: /{full_path}")
    return {"message": f"DEFAULT PATH HIT for /{full_path}"}