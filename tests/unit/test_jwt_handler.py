# tests/unit/test_jwt_handler.py

from jose import jwt
import pytest
from datetime import datetime, timedelta, timezone
from src.security.auth.jwt_handler import create_jwt, verify_jwt
from src.config.config import settings


@pytest.mark.unit
def test_create_jwt_and_verify():
    """Test the creation and verification of a JWT token."""
    payload = {"user": "mktakeda"}
    token = create_jwt(payload.copy())
    decoded = verify_jwt(token)

    assert decoded["user"] == "mktakeda"
    assert "exp" in decoded


@pytest.mark.unit
def test_verify_jwt_invalid_signature():
    """Test verification of a JWT token with an invalid signature."""
    payload = {"user": "fake", "exp": datetime.now(timezone.utc) + timedelta(minutes=5)}
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
    Cc5HJmxMmQKBgBpDPz+HL+DxcbjXVFrUa4m979cABv9AO5NtywrvVyaLPP681ozD
    6ptm7FtV0XqNpRVHkqgjGm1M80PsGx0X7SVJm0V4NpRBjCyiMwHqtnIzgY+uojbY
    0lnrVEXGtx5soMOklAijcxUV/HWLsqra7cJsyMS4XInur32KuXwGUm/vAoGAPOAc
    SzEf9wJHH1EIZuyDoa529lqxrPxSMoHXrIP06Yh5JvRO2od4R91FMS3enUAeVrV8
    mJEzxNXoGwrKEFKWdmQckEarhqttmK9qe45FgbKTeEkyHpYtkYrUaXU2VOmA3tP/
    zX2QZ8gu2PkSeXnXdK16AyeYlrgZKaipxjOmPgkCgYBT4OC/9x1xDzNTBY8weXeE
    NdZYIRW8xSB1U/Dthw9a0LBeIi9At9sf60cOXE1zkl1Ger3UTg4k75csMyZDZKv+
    1WMsLWcW9a14PugqFAjT+rKfYb+HpH5Q4v05QXeNRFwZ7iy01mpJ7xWzxPXFXfYA
    cct6nibrGliQGJz02sVVIQ==
    -----END PRIVATE KEY-----"""
    fake_token = jwt.encode(payload, fake_private_key, algorithm=settings.JWT_ALGORITHM)

    with pytest.raises(ValueError, match="Invalid Expired token"):
        verify_jwt(fake_token)


@pytest.mark.unit
def test_verify_jwt_expired_token():
    """Test verification of a JWT token with an expired token."""
    payload = {
        "user": "expired",
        "exp": datetime.now(timezone.utc) - timedelta(minutes=1),
    }
    token = jwt.encode(payload, settings.private_key, algorithm=settings.JWT_ALGORITHM)

    with pytest.raises(ValueError, match="Invalid Expired token"):
        verify_jwt(token)
