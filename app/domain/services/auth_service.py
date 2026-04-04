from __future__ import annotations

from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from passlib.context import CryptContext


class AuthService:
    def __init__(self, secret_key: str, algorithm: str = "HS256", token_minutes: int = 60):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.token_minutes = token_minutes
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, raw_password: str) -> str:
        return self.pwd_context.hash(raw_password)

    def verify_password(self, raw_password: str, password_hash: str) -> bool:
        return self.pwd_context.verify(raw_password, password_hash)

    def create_access_token(self, subject: str, role: str) -> str:
        now = datetime.now(timezone.utc)
        payload = {
            "sub": subject,
            "role": role,
            "iat": int(now.timestamp()),
            "exp": int((now + timedelta(minutes=self.token_minutes)).timestamp()),
        }
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def decode_token(self, token: str) -> dict:
        try:
            return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
        except JWTError as exc:
            raise ValueError("Invalid token") from exc
