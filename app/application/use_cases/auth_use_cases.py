from __future__ import annotations

from fastapi import HTTPException, status

from app.application.schemas.auth import LoginRequest, RegisterRequest, TokenResponse
from app.domain.entities.models import Role, User
from app.infrastructure.container import container


def register_user(payload: RegisterRequest) -> TokenResponse:
    role_value = payload.role.lower()
    allowed_roles = {r.value for r in Role}
    if role_value not in allowed_roles:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid role")

    if container.user_repo.get_by_email(payload.email):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

    user = User(
        email=payload.email,
        full_name=payload.full_name,
        password_hash=container.auth_service.hash_password(payload.password),
        role=Role(role_value),
    )
    container.user_repo.create(user)
    token = container.auth_service.create_access_token(subject=user.id, role=user.role.value)
    return TokenResponse(access_token=token)


def login_user(payload: LoginRequest) -> TokenResponse:
    user = container.user_repo.get_by_email(payload.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    if not container.auth_service.verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = container.auth_service.create_access_token(subject=user.id, role=user.role.value)
    return TokenResponse(access_token=token)
