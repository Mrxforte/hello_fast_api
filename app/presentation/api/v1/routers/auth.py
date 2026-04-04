from fastapi import APIRouter

from app.application.schemas.auth import LoginRequest, RegisterRequest, TokenResponse
from app.application.use_cases.auth_use_cases import login_user, register_user

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=TokenResponse)
def register(payload: RegisterRequest) -> TokenResponse:
    return register_user(payload)


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest) -> TokenResponse:
    return login_user(payload)
