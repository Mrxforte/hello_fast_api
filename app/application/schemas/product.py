from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class ProductCreateRequest(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    description: str = Field(min_length=3, max_length=500)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)


class ProductUpdateRequest(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=120)
    description: str | None = Field(default=None, min_length=3, max_length=500)
    price: float | None = Field(default=None, gt=0)
    stock: int | None = Field(default=None, ge=0)
    is_active: bool | None = None


class ProductResponse(BaseModel):
    id: str
    vendor_id: str
    name: str
    description: str
    price: float
    stock: int
    is_active: bool
    created_at: datetime
