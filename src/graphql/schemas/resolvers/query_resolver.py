from typing import List, Optional

import strawberry
from sqlalchemy.orm import Session

from src.graphql.schemas.types.user_type import UserType
from src.services.user import UserService
from src.utils.logger import logger


@strawberry.type
class Query:
    """GraphQL Query class to fetch user data."""

    @strawberry.field
    def user(self, id: int, info) -> Optional[UserType]:
        """Fetch a user by their ID.

        Args:
            id (int): The ID of the user to fetch.
            info: The GraphQL info object containing context.

        Returns:
            Optional[UserType]: The user object if found, otherwise None.
        """
        logger.info(f"🔍 Fetching user with id={id}")
        db: Session = info.context.db  # Retrieve the database session from the context
        user = UserService(db).get_user(id)  # Fetch the user from the UserService
        logger.success(f"✅ Found user id={id}")
        return UserType(id=user["id"], name=user["name"])  # Return the user as a UserType object

    @strawberry.field
    def users(self, info) -> List[UserType]:
        """Fetch all users.

        Args:
            info: The GraphQL info object containing context.

        Returns:
            List[UserType]: A list of user objects.
        """
        logger.info("🔍 Fetching all users")
        db: Session = info.context.db  # Retrieve the database session from the context
        result = UserService(db).get_users()  # Fetch all users from the UserService
        logger.success(f"✅ Found {len(result['users'])} users")
        return [UserType(id=u["id"], name=u["name"]) for u in result["users"]]  # Return a list of UserType objects