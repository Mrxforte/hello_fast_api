from fastapi import APIRouter, Depends, Response, status

from app.application.schemas.product import ProductCreateRequest, ProductResponse, ProductUpdateRequest
from app.application.use_cases.product_use_cases import (
    create_product,
    delete_product,
    list_products,
    list_vendor_products,
    update_product,
)
from app.domain.entities.models import Role, User
from app.infrastructure.security.dependencies import require_roles

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("", response_model=ProductResponse)
def create_new_product(
    payload: ProductCreateRequest,
    current_user: User = Depends(require_roles(Role.VENDOR)),
) -> ProductResponse:
    product = create_product(current_user, payload)
    return ProductResponse(**product.__dict__)


@router.patch("/{product_id}", response_model=ProductResponse)
def patch_product(
    product_id: str,
    payload: ProductUpdateRequest,
    current_user: User = Depends(require_roles(Role.VENDOR)),
) -> ProductResponse:
    product = update_product(current_user, product_id, payload)
    return ProductResponse(**product.__dict__)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_product(
    product_id: str,
    current_user: User = Depends(require_roles(Role.VENDOR)),
) -> Response:
    delete_product(current_user, product_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("", response_model=list[ProductResponse])
def get_all_products() -> list[ProductResponse]:
    items = list_products()
    return [ProductResponse(**item.__dict__) for item in items]


@router.get("/vendor/{vendor_id}", response_model=list[ProductResponse])
def get_vendor_products(vendor_id: str) -> list[ProductResponse]:
    items = list_vendor_products(vendor_id)
    return [ProductResponse(**item.__dict__) for item in items]
