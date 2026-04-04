from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class OrderCreateItem(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)


class OrderCreateRequest(BaseModel):
    items: list[OrderCreateItem] = Field(min_length=1)


class OrderItemResponse(BaseModel):
    product_id: str
    quantity: int
    unit_price: float


class OrderResponse(BaseModel):
    id: str
    customer_id: str
    vendor_id: str
    total_amount: float
    status: str
    created_at: datetime
    confirmed_at: datetime | None
    items: list[OrderItemResponse]
