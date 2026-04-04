from fastapi import APIRouter, Depends

from app.application.schemas.order import OrderCreateRequest, OrderItemResponse, OrderResponse
from app.application.use_cases.order_use_cases import confirm_order, create_order, get_my_orders
from app.domain.entities.models import Role, User
from app.infrastructure.security.dependencies import require_roles

router = APIRouter(prefix="/orders", tags=["Orders"])


def _to_response(order) -> OrderResponse:
    return OrderResponse(
        id=order.id,
        customer_id=order.customer_id,
        vendor_id=order.vendor_id,
        total_amount=order.total_amount,
        status=order.status.value,
        created_at=order.created_at,
        confirmed_at=order.confirmed_at,
        items=[OrderItemResponse(**item.__dict__) for item in order.items],
    )


@router.post("", response_model=OrderResponse)
def create_new_order(
    payload: OrderCreateRequest,
    current_user: User = Depends(require_roles(Role.CUSTOMER)),
) -> OrderResponse:
    order = create_order(current_user, payload)
    return _to_response(order)


@router.patch("/{order_id}/confirm", response_model=OrderResponse)
def confirm_vendor_order(
    order_id: str,
    current_user: User = Depends(require_roles(Role.VENDOR)),
) -> OrderResponse:
    order = confirm_order(current_user, order_id)
    return _to_response(order)


@router.get("/me", response_model=list[OrderResponse])
def list_my_orders(
    current_user: User = Depends(require_roles(Role.CUSTOMER, Role.VENDOR, Role.ADMIN)),
) -> list[OrderResponse]:
    orders = get_my_orders(current_user)
    return [_to_response(order) for order in orders]
