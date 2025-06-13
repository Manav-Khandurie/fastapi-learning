# tests/unit/test_jwt_handler.py

from jose import jwt
import pytest
from datetime import datetime, timedelta, timezone
from src.security.auth.jwt_handler import create_jwt, verify_jwt
from src.config.config import settings


@pytest.mark.unit
def test_create_jwt_and_verify():
    """Test the creation and verification of a JWT token."""
    payload = {"user": "mktakeda"}  # Payload containing user information
    token = create_jwt(payload.copy())  # Create a JWT token with the payload
    decoded = verify_jwt(token)  # Verify the created token

    assert decoded["user"] == "mktakeda"  # Check if the user in the decoded token matches the original payload
    assert "exp" in decoded  # Ensure that the expiration claim is present in the decoded token


@pytest.mark.unit
def test_verify_jwt_invalid_signature():
    """Test verification of a JWT token with an invalid signature."""
    payload = {"user": "fake", "exp": datetime.now(timezone.utc) + timedelta(minutes=5)}  # Payload with expiration
    fake_private_key = """-----BEGIN PRIVATE KEY-----
    MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCgu4+HhVwmvK7m
    xh3v8d4RjLAYpnwE2be1nsEvkhlTB/dyscFyo5OQqm1yTfLW6m4Y+oM8z1+LVLA3
    JBsqyTX6y801xNNFFPHI2bp7LoNXXfuNUEX9Aq8KZrT2QBvel+VEW9PrvbWxqIVj
    VakNit6O3XmDyUFGfnRpKiYT3xQwOu9qczgp+o3jxetYpsdGhsk+t0DrDpAa+oSK
    vAFAq4+3jctxGN4csPw3d6/jAX9+RvuWxRU7BHY/mMXZv1j8LQQBM71tXEJJEJM0
    mNdVQE7kGeIABSgDknamjfgOroI9oGyVTDLZB1+6j+6OB6B7j3tqA4MzqjvNTdun
    HjPJxZGfAgMBAAECggEAEucsEKCe/1FGco6PO8ZiuwakOSnvQPTH9byndKxGfSzd
    Lah5Gz3gn21jtMM1EZB9hUOFBrROxMifdsSwyz3hss6gIjg1LpUxgFEW7ODCApbj
    fDGaIZDcvCjrFGDixjFv/bOc/0cO5MdwdIfA+34/AWdLoLOdESjTEQErfD/KlIdS
    JEusY2HC6L5UNe6asdGXZdPoyoG/XUJm0t5qOHDCqcr5SL1Tkr+fRDbA7k2gqjtF
    wp7lhKyt19w9QA/9cSYbHhYXpIBlipImK9SXKG6MuAqYwQE1UjKd1fLfusPfkI+i
    leNeTCS0vd1sTDIQ5rEwFw//ycHIvNDfSriOefP0uQKBgQDNkBUevZrNcJCgPgql
    EI1R9D8iZGgNrH7vUU/aKRg99Kxgyy0V0FiF1zTPXIM8qdxROdB6eVYzpty2kkzH
    UPAbmeX7w9S4jSUXpT53mUfolBhvTAkYZkcT5Oq5MG0/MI7aKMbFbyEwjemqlGo7
    i/VHeBo3vcDH7uv7DbK7DHU69wKBgQDIK5U6pwrUWGVwbaKsM99aLmBRMoRej05s
    190lJ2LbKt7KQ+sTE/UmnfkR4UyoCekYq/NjOD/jWl8wRIAFTNuMLWdwsvHF2mvD
    5tCAWZ2WI2NjNIaN4dFfHgQ+CIAPNJ7PtCZLkVuVmvLzwiJ7LldmPWeY9ThnRvAI
    Cc5HJmx