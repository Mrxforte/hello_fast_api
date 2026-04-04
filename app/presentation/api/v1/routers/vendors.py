from fastapi import APIRouter, Depends

from app.application.schemas.vendor import VendorCreateRequest, VendorResponse
from app.application.use_cases.vendor_use_cases import (
    create_vendor_profile,
    get_current_vendor,
    list_vendors,
)
from app.domain.entities.models import Role, User
from app.infrastructure.security.dependencies import require_roles

router = APIRouter(prefix="/vendors", tags=["Vendors"])


@router.post("/me", response_model=VendorResponse)
def create_my_vendor(
    payload: VendorCreateRequest,
    current_user: User = Depends(require_roles(Role.VENDOR)),
) -> VendorResponse:
    vendor = create_vendor_profile(current_user, payload)
    return VendorResponse(**vendor.__dict__)


@router.get("/me", response_model=VendorResponse)
def get_my_vendor(
    current_user: User = Depends(require_roles(Role.VENDOR)),
) -> VendorResponse:
    vendor = get_current_vendor(current_user)
    return VendorResponse(**vendor.__dict__)


@router.get("", response_model=list[VendorResponse])
def get_vendors() -> list[VendorResponse]:
    vendors = list_vendors()
    return [VendorResponse(**vendor.__dict__) for vendor in vendors]
