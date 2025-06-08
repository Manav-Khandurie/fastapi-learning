from typing import Optional

from fastapi import Header, HTTPException, status

from src.security.auth.jwt_handler import verify_jwt
from src.utils.logger import logger


def get_current_user(authorization: Optional[str] = Header(None)):
    """
    Retrieve the current user based on the provided Authorization header.

    Args:
        authorization (Optional[str]): The Authorization header containing the Bearer token.

    Raises:
        HTTPException: If the Authorization header is missing or invalid, or if token verification fails.

    Returns:
        dict: The payload of the verified JWT token.
    """
    logger.info("🔑 Authenticating user from Authorization header")
    if authorization is None or not authorization.startswith("Bearer "):
        logger.warning("⚠️ Missing or invalid Authorization header")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing or invalid token"
        )

    token = authorization.split(" ")[1]  # Extract the token from the header
    try:
        payload = verify_jwt(token)  # Verify the JWT token
        logger.success("✅ Token verified successfully")
        return payload
    except ValueError:
        logger.warning("❌ Token verification failed")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token verification failed"
        )