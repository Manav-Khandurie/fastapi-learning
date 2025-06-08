from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.dependency import get_db
from src.schema.user import (
    UserAddRequest,
    UserFetchAllResponse,
    UserFetchResponse,
    UserQueryResponse,
)
from src.services.user import UserService
from src.utils.logger import logger

router = APIRouter()


@router.get("/user/{id}", response_model=UserFetchResponse)
def get_user(id: int, db: Session = Depends(get_db)) -> dict:
    """Fetch a user by their ID."""
    logger.info(f"Fetching user with id={id}")
    return UserService(db).get_user(id)


@router.get("/users", response_model=UserFetchAllResponse)
def get_users(db: Session = Depends(get_db)) -> dict:
    """Fetch all users."""
    logger.info("Fetching all users")
    return UserService(db).get_users()


@router.post("/user", response_model=UserQueryResponse)
def add_user(payload: UserAddRequest, db: Session = Depends(get_db)) -> dict:
    """Add a new user with the provided details."""
    logger.info(f"Adding user with id={payload.id}, name={payload.name}")
    return UserService(db).add_user(payload.id, payload.name)


@router.put("/user/{id}", response_model=UserQueryResponse)
def update_user(
    id: int, payload: UserAddRequest, db: Session = Depends(get_db)
) -> dict:
    """Update an existing user's name by their ID."""
    logger.info(f"Updating user with id={id} to name={payload.name}")
    return UserService(db).update_user(id, payload.name)


@router.delete("/user/{id}", response_model=UserQueryResponse)
def delete_user(id: int, db: Session = Depends(get_db)) -> dict:
    """Delete a user by their ID."""
    logger.info(f"Deleting user with id={id}")
    return UserService(db).delete_user(id)


@router.delete("/users", response_model=UserQueryResponse)
def delete_users(db: Session = Depends(get_db)) -> dict:
    """Delete all users."""
    logger.info("Deleting all users")
    return UserService(db).delete_users()