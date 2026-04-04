from __future__ import annotations

from fastapi import HTTPException, status

from app.application.schemas.vendor import VendorCreateRequest
from app.domain.entities.models import Role, User, Vendor
from app.infrastructure.container import container


def create_vendor_profile(current_user: User, payload: VendorCreateRequest) -> Vendor:
    if current_user.role != Role.VENDOR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only vendors can create vendor profile")

    if container.vendor_repo.get_by_owner(current_user.id):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Vendor profile already exists")

    vendor = Vendor(owner_user_id=current_user.id, name=payload.name, description=payload.description)
    return container.vendor_repo.create(vendor)


def get_current_vendor(current_user: User) -> Vendor:
    vendor = container.vendor_repo.get_by_owner(current_user.id)
    if not vendor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vendor profile not found")
    return vendor


def list_vendors() -> list[Vendor]:
    return container.vendor_repo.list_all()
