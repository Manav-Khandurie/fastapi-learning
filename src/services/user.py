from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.model.user import User
from src.utils.logger import logger


class UserService:
    """Service class for managing user-related operations."""

    def __init__(self, db: Session):
        """Initialize UserService with a database session.

        Args:
            db (Session): The database session to be used for operations.
        """
        self.db = db

    def get_user(self, id: int) -> dict:
        """Fetch a user by their ID.

        Args:
            id (int): The ID of the user to fetch.

        Returns:
            dict: A dictionary containing the user's ID and name.

        Raises:
            HTTPException: If the user is not found.
        """
        logger.info(f"🔍 Fetching user with ID {id}")
        user = self.db.query(User).filter(User.id == id).first()
        if user is None:
            logger.warning(f"❌ User with ID {id} not found")
            raise HTTPException(status_code=404, detail="NO USER FOUND")
        return {"id": user.id, "name": user.name}

    def get_users(self) -> dict:
        """Fetch all users.

        Returns:
            dict: A dictionary containing a list of all users with their IDs and names.
        """
        logger.info("📄 Fetching all users")
        users = self.db.query(User).all()
        return {"users": [{"id": user.id, "name": user.name} for user in users]}

    def add_user(self, id: int, name: str) -> dict:
        """Add a new user.

        Args:
            id (int): The ID of the user to add.
            name (str): The name of the user to add.

        Returns:
            dict: A message indicating the record was inserted.

        Raises:
            HTTPException: If the ID already exists.
        """
        logger.info(f"➕ Adding user with ID {id}")
        if self.db.query(User).filter(User.id == id).first():
            logger.warning(f"⚠️ ID {id} already exists")
            raise HTTPException(status_code=400, detail="ID already taken")
        new_user = User(id=id, name=name)
        self.db.add(new_user)
        self.db.commit()
        logger.success(f"✅ User with ID {id} added")
        return {"message": "Record Inserted"}

    def update_user(self, id: int, name: str) -> dict:
        """Update an existing user's name.

        Args:
            id (int): The ID of the user to update.
            name (str): The new name for the user.

        Returns:
            dict: A message indicating the record was updated.

        Raises:
            HTTPException: If the user ID is not found.
        """
        logger.info(f"🔄 Updating user with ID {id}")
        user = self.db.query(User).filter(User.id == id).first()
        if not user:
            logger.warning(f"❌ ID {id} not found for update")
            raise HTTPException(status_code=400, detail="ID not found")
        user.name = name  # type: ignore
        self.db.commit()
        logger.success(f"✅ User with ID {id} updated")
        return {"message": "Record Updated"}

    def delete_user(self, id: int) -> dict:
        """Delete a user by their ID.

        Args:
            id (int): The ID of the user to delete.

        Returns:
            dict: A message indicating the record was deleted.

        Raises:
            HTTPException: If the user ID is not found.
        """
        logger.info(f"🗑️ Deleting user with ID {id}")
        user = self.db.query(User).filter(User.id == id).first()
        if not user:
            logger.warning(f"❌ ID {id} not found for deletion")
            raise HTTPException(status_code=400, detail="ID not found")
        self.db.delete(user)
        self.db.commit()
        logger.success(f"✅ User with ID {id} deleted")
        return {"message": "Record Deleted"}

    def delete_users(self) -> dict:
        """Delete all users.

        Returns:
            dict: A message indicating all records were deleted.
        """
        logger.info("🗑️ Deleting all users")
        self.db.query(User).delete()
        self.db.commit()
        logger.success("✅ All user records deleted")
        return {"message": "All Records Deleted"}