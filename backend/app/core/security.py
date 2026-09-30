"""JWT creation/verification and password hashing primitives.

Full auth flows (login, refresh rotation, OAuth) are implemented in the
auth module; this module provides only the cryptographic primitives.
"""

from datetime import UTC, datetime, timedelta

import jwt

from app.core.config import settings


def create_access_token(subject: str, expires_delta: timedelta | None = None) -> str:
    now = datetime.now(UTC)
    payload = {
        "sub": subject,
        "type": "access",
        "iat": now,
        "exp": now + (expires_delta or timedelta(minutes=settings.access_token_expire_minutes)),
    }
    return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)


def create_refresh_token(subject: str) -> str:
    now = datetime.now(UTC)
    payload = {
        "sub": subject,
        "type": "refresh",
        "iat": now,
        "exp": now + timedelta(days=settings.refresh_token_expire_days),
    }
    return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)


def decode_token(token: str) -> dict:
    """Decode and verify a JWT.

    Raises jwt.InvalidTokenError / jwt.ExpiredSignatureError on failure.
    """
    return jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
