# tests/unit/test_user_service.py

import pytest
from unittest.mock import MagicMock
from fastapi import HTTPException

from src.services.user import UserService
from src.model.user import User


@pytest.mark.unit
def test_get_user_found():
    """Test case for retrieving a user that exists in the database."""
    db = MagicMock()
    db.query().filter().first.return_value = User(id=1, name="Alice")

    service = UserService(db)
    result = service.get_user(1)

    assert result == {"id": 1, "name": "Alice"}


@pytest.mark.unit
def test_get_user_not_found():
    """Test case for attempting to retrieve a user that does not exist."""
    db = MagicMock()
    db.query().filter().first.return_value = None

    service = UserService(db)

    with pytest.raises(HTTPException) as e:
        service.get_user(99)

    assert e.value.status_code == 404
    assert e.value.detail == "NO USER FOUND"


@pytest.mark.unit
def test_get_users():
    """Test case for retrieving all users from the database."""
    db = MagicMock()
    db.query().all.return_value = [User(id=1, name="Alice"), User(id=2, name="Bob")]

    service = UserService(db)
    result = service.get_users()

    assert result == {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
        ]
    }


@pytest.mark.unit
def test_add_user_success():
    """Test case for successfully adding a new user."""
    db = MagicMock()
    db.query().filter().first.return_value = None

    service = UserService(db)
    result = service.add_user(1, "Alice")

    db.add.assert_called()
    db.commit.assert_called()
    assert result == {"message": "Record Inserted"}


@pytest.mark.unit
def test_add_user_duplicate_id():
    """Test case for attempting to add a user with a duplicate ID."""
    db = MagicMock()
    db.query().filter().first.return_value = User(id=1, name="Alice")

    service = UserService(db)

    with pytest.raises(HTTPException) as e:
        service.add_user(1, "Alice")

    assert e.value.status_code == 400
    assert e.value.detail == "ID already taken"


@pytest.mark.unit
def test_update_user_success():
    """Test case for successfully updating an existing user."""
    db = MagicMock()
    user = User(id=1, name="Alice")
    db.query().filter().first.return_value = user

    service = UserService(db)
    result = service.update_user(1, "AliceUpdated")

    assert user.name == "AliceUpdated"
    db.commit.assert_called()
    assert result == {"message": "Record Updated"}


@pytest.mark.unit
def test_update_user_not_found():
    """Test case for attempting to update a user that does not exist."""
    db = MagicMock()
    db.query().filter().first.return_value = None

    service = UserService(db)

    with pytest.raises(HTTPException) as e:
        service.update_user(1, "NewName")

    assert e.value.status_code == 400
    assert e.value.detail == "ID not found"


@pytest.mark.unit
def test_delete_user_success():
    """Test case for successfully deleting an existing user."""
    db = MagicMock()
    user = User(id=1, name="Alice")
    db.query().filter().first.return_value = user

    service = UserService(db)
    result = service.delete_user(1)

    db.delete.assert_called_with(user)
    db.commit.assert_called()
    assert result == {"message": "Record Deleted"}


@pytest.mark.unit
def test_delete_user_not_found():
    """Test case for attempting to delete a user that does not exist."""
    db = MagicMock()
    db.query().filter().first.return_value = None

    service = UserService(db)

    with pytest.raises(HTTPException) as e:
        service.delete_user(99)

    assert e.value.status_code == 400
    assert e.value.detail == "ID not found"


@pytest.mark.unit
def test_delete_users():
    """Test case for deleting all users from the database."""
    db = MagicMock()

    service = UserService(db)
    result = service.delete_users()

    db.query().delete.assert_called()
    db.commit.assert_called()
    assert result == {"message": "All Records Deleted"}