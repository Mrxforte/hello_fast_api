from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import uuid4


class Role(str, Enum):
    ADMIN = "admin"
    VENDOR = "vendor"
    CUSTOMER = "customer"


class OrderStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"


@dataclass
class User:
    email: str
    full_name: str
    password_hash: str
    role: Role
    id: str = field(default_factory=lambda: str(uuid4()))
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Vendor:
    owner_user_id: str
    name: str
    description: str
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Product:
    vendor_id: str
    name: str
    description: str
    price: float
    stock: int
    id: str = field(default_factory=lambda: str(uuid4()))
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class OrderItem:
    product_id: str
    quantity: int
    unit_price: float


@dataclass
class Order:
    customer_id: str
    vendor_id: str
    items: list[OrderItem]
    total_amount: float
    id: str = field(default_factory=lambda: str(uuid4()))
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime = field(default_factory=datetime.utcnow)
    confirmed_at: Optional[datetime] = None
