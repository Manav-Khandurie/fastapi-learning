# tests/conftest.py

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app
from src.database.base import Base
from src.database.dependency import get_db


# Use in-memory SQLite for tests
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./data/test_db.db"

engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def override_get_db():
    """Override the default database session for testing.

    Yields a database session for use in tests, ensuring that
    the session is properly closed and rolled back after use.
    """
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.rollback()  # Rollback any changes made during the test
        db.close()  # Close the database session


# Apply override
app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="module")
def test_client():
    """Fixture to create a test client for the FastAPI application.

    This fixture sets up the database tables before tests run
    and drops them after all tests in the module have completed.
    """
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)  # Make sure this is called
    with TestClient(app) as c:
        yield c
    print("Dropping tables...")
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def auth_token(test_client):
    """Fixture to obtain an authentication token for a test user.

    This fixture makes a request to the token endpoint and
    returns the access token for use in tests.
    """
    response = test_client.get("/api/v1/token/testuser")

    assert response.status_code == 200  # Ensure the request was successful
    return response.json()["access_token"]  # Return the access token from the response
