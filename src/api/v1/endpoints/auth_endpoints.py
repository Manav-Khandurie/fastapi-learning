from fastapi import APIRouter

from src.security.auth.jwt_handler import create_jwt
from src.utils.logger import logger

router = APIRouter()


@router.get("/token/{user}")
def get_jwt_token(user: str) -> dict:
    """
    Generate a JWT token for the specified user.

    Args:
        user (str): The username for which the JWT token is generated.

    Returns:
        dict: A dictionary containing the access token and its type.
    """
    token = create_jwt({user: user})
    logger.info(f"JWT token generated for user: {user}")  # log token generation
    return {"access_token": token, "token_type": "bearer"}