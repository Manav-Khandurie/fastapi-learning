import pytest


@pytest.mark.e2e
def test_full_crud_flow(test_client):
    """Test the full CRUD flow for user management API.

    This test performs the following steps:
    1. Health Check
    2. Authenticate and Get Token
    3. Read All Users (initial state)
    4. Create a New User
    5. Read the Created User
    6. Update the Created User
    7. Confirm Update
    8. Delete the Created User
    9. Delete All Users
    10. Confirm No Users Exist
    """

    # Step 1: Health Check
    health_res = test_client.get("/api/v1/health")
    assert health_res.status_code == 200
    assert health_res.json() == {"message": "Healthy"}

    # Step 2: Authenticate and Get Token
    token_res = test_client.get("/api/v1/token/testuser")
    assert token_res.status_code == 200
    token = token_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Step 3: Read All Users (initial state)
    users_res = test_client.get("/api/v1/users", headers=headers)
    assert users_res.status_code == 200
    # initial_user_count = len(users_res.json()["users"])

    # Step 4: Create a New User
    user_data = {"id": 12345, "name": "TestUser"}
    create_res = test_client.post("/api/v1/user", json=user_data, headers=headers)
    assert create_res.status_code == 200
    assert create_res.json() == {"message": "Record Inserted"}

    # Step 5: Read the Created User
    get_user_res = test_client.get(f"/api/v1/user/{user_data['id']}", headers=headers)
    assert get_user_res.status_code == 200
    assert get_user_res.json() == {**user_data, "msg": None}

    # Step 6: Update the Created User
    updated_user_data = {"id": 999, "name": "TestUserUpdated"}
    update_res = test_client.put(
        f"/api/v1/user/{user_data['id']}", json=updated_user_data, headers=headers
    )
    assert update_res.status_code == 200
    assert update_res.json()["message"] == "Record Updated"

    # Step 7: Confirm Update
    get_updated_res = test_client.get(
        f"/api/v1/user/{user_data['id']}", headers=headers
    )
    assert get_updated_res.status_code == 200
    assert get_updated_res.json()["name"] == "TestUserUpdated"

    # Step 8: Delete the Created User
    delete_res = test_client.delete(f"/api/v1/user/{user_data['id']}", headers=headers)
    assert delete_res.status_code == 200
    assert delete_res.json()["message"] == "Record Deleted"

    # Step 9: Delete All Users
    delete_all_res = test_client.delete("/api/v1/users", headers=headers)
    assert delete_all_res.status_code == 200
    assert delete_all_res.json()["message"] == "All Records Deleted"

    # Step 10: Confirm No Users Exist
    final_users_res = test_client.get("/api/v1/users", headers=headers)
    assert final_users_res.status_code == 200
    assert final_users_res.json()["users"] == []