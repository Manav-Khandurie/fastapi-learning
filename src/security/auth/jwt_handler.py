from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt

from src.config.config import settings
from src.utils.logger import logger


def create_jwt(payload: dict) -> str:
    """Create a JSON Web Token (JWT) with the given payload.

    Args:
        payload (dict): The payload to encode in the JWT.

    Returns:
        str: The encoded JWT as a string.
    """
    logger.info("🔐 Creating JWT token")
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.JWT_EXPIRATION_MINUTES
    )
    payload.update({"exp": expire})  # Add expiration time to the payload
    token = jwt.encode(payload, settings.private_key, algorithm=settings.JWT_ALGORITHM)
    logger.success("✅ JWT token created successfully")
    return token


def verify_jwt(token: str) -> str:
    """Verify a JSON Web Token (JWT) and decode its payload.

    Args:
        token (str): The JWT to verify.

    Returns:
        str: The decoded payload of the JWT.

    Raises:
        ValueError: If the token is invalid or expired.
    """
    logger.info("🔍 Verifying JWT token")
    try:
        decoded_token = jwt.decode(
            token, settings.public_key, algorithms=[settings.JWT_ALGORITHM]
        )
        logger.success("✅ JWT token verified successfully")
        return decoded_token
    except JWTError as e:
        logger.warning(f"❌ JWT verification failed: {e}")
        raise ValueError("Invalid Expired token") from e