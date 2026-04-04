from __future__ import annotations

from fastapi import HTTPException, status

from app.application.schemas.product import ProductCreateRequest, ProductUpdateRequest
from app.domain.entities.models import Product, Role, User
from app.infrastructure.container import container


def create_product(current_user: User, payload: ProductCreateRequest) -> Product:
    if current_user.role != Role.VENDOR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only vendors can create products")

    vendor = container.vendor_repo.get_by_owner(current_user.id)
    if not vendor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vendor profile not found")

    product = Product(
        vendor_id=vendor.id,
        name=payload.name,
        description=payload.description,
        price=payload.price,
        stock=payload.stock,
    )
    return container.product_repo.create(product)


def update_product(current_user: User, product_id: str, payload: ProductUpdateRequest) -> Product:
    product = container.product_repo.get_by_id(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    vendor = container.vendor_repo.get_by_owner(current_user.id)
    if not vendor or vendor.id != product.vendor_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Cannot update this product")

    if payload.name is not None:
        product.name = payload.name
    if payload.description is not None:
        product.description = payload.description
    if payload.price is not None:
        product.price = payload.price
    if payload.stock is not None:
        product.stock = payload.stock
    if payload.is_active is not None:
        product.is_active = payload.is_active

    return container.product_repo.update(product)


def delete_product(current_user: User, product_id: str) -> None:
    product = container.product_repo.get_by_id(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    vendor = container.vendor_repo.get_by_owner(current_user.id)
    if not vendor or vendor.id != product.vendor_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Cannot delete this product")

    container.product_repo.delete(product_id)


def list_products() -> list[Product]:
    return container.product_repo.list_all()


def list_vendor_products(vendor_id: str) -> list[Product]:
    return container.product_repo.list_by_vendor(vendor_id)
