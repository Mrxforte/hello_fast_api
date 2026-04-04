from __future__ import annotations

from datetime import datetime

from fastapi import HTTPException, status

from app.application.schemas.order import OrderCreateRequest
from app.domain.entities.models import Order, OrderItem, OrderStatus, Role, User
from app.infrastructure.container import container


def create_order(current_user: User, payload: OrderCreateRequest) -> Order:
    if current_user.role != Role.CUSTOMER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only customers can create orders")

    if not payload.items:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order items are required")

    products = []
    for item in payload.items:
        product = container.product_repo.get_by_id(item.product_id)
        if not product or not product.is_active:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product not found: {item.product_id}")
        if product.stock < item.quantity:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Insufficient stock for {product.name}")
        products.append((item, product))

    vendor_id = products[0][1].vendor_id
    if any(p.vendor_id != vendor_id for _, p in products):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="All items in one order must belong to the same vendor",
        )

    order_items: list[OrderItem] = []
    total_amount = 0.0
    for req_item, product in products:
        product.stock -= req_item.quantity
        container.product_repo.update(product)
        line_price = product.price * req_item.quantity
        total_amount += line_price
        order_items.append(
            OrderItem(product_id=product.id, quantity=req_item.quantity, unit_price=product.price)
        )

    order = Order(
        customer_id=current_user.id,
        vendor_id=vendor_id,
        items=order_items,
        total_amount=round(total_amount, 2),
    )
    return container.order_repo.create(order)


def confirm_order(current_user: User, order_id: str) -> Order:
    order = container.order_repo.get_by_id(order_id)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")

    vendor = container.vendor_repo.get_by_owner(current_user.id)
    if not vendor or vendor.id != order.vendor_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Cannot confirm this order")

    order.status = OrderStatus.CONFIRMED
    order.confirmed_at = datetime.utcnow()
    return container.order_repo.update(order)


def get_my_orders(current_user: User) -> list[Order]:
    if current_user.role == Role.CUSTOMER:
        return container.order_repo.list_by_customer(current_user.id)
    if current_user.role == Role.VENDOR:
        vendor = container.vendor_repo.get_by_owner(current_user.id)
        if not vendor:
            return []
        return container.order_repo.list_by_vendor(vendor.id)
    return container.order_repo.list_all()
