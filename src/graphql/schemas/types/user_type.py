import strawberry


@strawberry.type
class UserType:
    """Represents a user with an ID and a name."""
    
    id: int  # Unique identifier for the user
    name: str  # Name of the user