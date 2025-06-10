import pytest


# Test Create User
@pytest.mark.integration
def test_create_user(test_client, auth_token):
    """Test the creation of a new user.

    Args:
        test_client: The test client used to make requests.
        auth_token: The authorization token for the request.

    Asserts:
        The response status code is 200 and the response JSON indicates
        that the record was inserted successfully.
    """
    response = test_client.post(
        "/api/v1/user",
        json={"id": 1, "name": "John Doe"},
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Record Inserted"}


# Test Get User
@pytest.mark.integration
def test_get_user(test_client, auth_token):
    """Test retrieving an existing user by ID.

    Args:
        test_client: The test client used to make requests.
        auth_token: The authorization token for the request.

    Asserts:
        The response status code is 200 and the response JSON contains
        the user's details.
    """
    # Assume user with ID 1 exists
    response = test_client.get(
        "/api/v1/user/1", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "msg": None}


# Test Update User
@pytest.mark.integration
def test_update_user(test_client, auth_token):
    """Test updating an existing user's information.

    Args:
        test_client: The test client used to make requests.
        auth_token: The authorization token for the request.

    Asserts:
        The response status code is 200 and the response JSON indicates
        that the record was updated successfully.
    """
    response = test_client.put(
        "/api/v1/user/1",
        json={"id": 0, "name": "John Updated"},
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Record Updated"}


# Test Delete User
@pytest.mark.integration
def test_delete_user(test_client, auth_token):
    """Test deleting an existing user by ID.

    Args:
        test_client: The test client used to make requests.
        auth_token: The authorization token for the request.

    Asserts:
        The response status code is 200 and the response JSON indicates
        that the record was deleted successfully.
    """
    response = test_client.delete(
        "/api/v1/user/1", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Record Deleted"}


# Test To get Deleted User
@pytest.mark.integration
def test_get_deleted_user(test_client, auth_token):
    """Test retrieving a user that has been deleted.

    Args:
        test_client: The test client used to make requests.
        auth_token: The authorization token for the request.

    Asserts:
        The response status code is 404 and the response JSON indicates
        that no user was found.
    """
    response = test_client.get(
        "/api/v1/user/1", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "NO USER FOUND"}
