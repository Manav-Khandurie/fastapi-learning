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
    """Fetch a user by their ID.

    Args:
        id (int): The ID of the user to fetch.
        db (Session, optional): The database session dependency.

    Returns:
        dict: The fetched user data.
    """
    logger.info(f"Fetching user with id={id}")
    return UserService(db).get_user(id)


@router.get("/users", response_model=UserFetchAllResponse)
def get_users(db: Session = Depends(get_db)) -> dict:
    """Fetch all users.

    Args:
        db (Session, optional): The database session dependency.

    Returns:
        dict: The list of all users.
    """
    logger.info("Fetching all users")
    return UserService(db).get_users()


@router.post("/user", response_model=UserQueryResponse)
def add_user(payload: UserAddRequest, db: Session = Depends(get_db)) -> dict:
    """Add a new user.

    Args:
        payload (UserAddRequest): The user data to add.
        db (Session, optional): The database session dependency.

    Returns:
        dict: The added user data.
    """
    logger.info(f"Adding user with id={payload.id}, name={payload.name}")
    return UserService(db).add_user(payload.id, payload.name)


@router.put("/user/{id}", response_model=UserQueryResponse)
def update_user(
    id: int, payload: UserAddRequest, db: Session = Depends(get_db)
) -> dict:
    """Update an existing user.

    Args:
        id (int): The ID of the user to update.
        payload (UserAddRequest): The new user data.
        db (Session, optional): The database session dependency.

    Returns:
        dict: The updated user data.
    """
    logger.info(f"Updating user with id={id} to name={payload.name}")
    return UserService(db).update_user(id, payload.name)


@router.delete("/user/{id}", response_model=UserQueryResponse)
def delete_user(id: int, db: Session = Depends(get_db)) -> dict:
    """Delete a user by their ID.

    Args:
        id (int): The ID of the user to delete.
        db (Session, optional): The database session dependency.

    Returns:
        dict: The deleted user data.
    """
    logger.info(f"Deleting user with id={id}")
    return UserService(db).delete_user(id)


@router.delete("/users", response_model=UserQueryResponse)
def delete_users(db: Session = Depends(get_db)) -> dict:
    """Delete all users.

    Args:
        db (Session, optional): The database session dependency.

    Returns:
        dict: The result of the deletion operation.
    """
    logger.info("Deleting all users")
    return UserService(db).delete_users()
