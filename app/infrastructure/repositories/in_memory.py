from __future__ import annotations

from typing import Optional

from app.domain.entities.models import Order, Product, User, Vendor
from app.domain.repositories.contracts import (
    OrderRepository,
    ProductRepository,
    UserRepository,
    VendorRepository,
)


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._items: dict[str, User] = {}

    def create(self, user: User) -> User:
        self._items[user.id] = user
        return user

    def get_by_email(self, email: str) -> Optional[User]:
        return next((u for u in self._items.values() if u.email == email), None)

    def get_by_id(self, user_id: str) -> Optional[User]:
        return self._items.get(user_id)

    def list_all(self) -> list[User]:
        return list(self._items.values())


class InMemoryVendorRepository(VendorRepository):
    def __init__(self):
        self._items: dict[str, Vendor] = {}

    def create(self, vendor: Vendor) -> Vendor:
        self._items[vendor.id] = vendor
        return vendor

    def get_by_id(self, vendor_id: str) -> Optional[Vendor]:
        return self._items.get(vendor_id)

    def get_by_owner(self, owner_user_id: str) -> Optional[Vendor]:
        return next((v for v in self._items.values() if v.owner_user_id == owner_user_id), None)

    def list_all(self) -> list[Vendor]:
        return list(self._items.values())


class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self._items: dict[str, Product] = {}

    def create(self, product: Product) -> Product:
        self._items[product.id] = product
        return product

    def get_by_id(self, product_id: str) -> Optional[Product]:
        return self._items.get(product_id)

    def update(self, product: Product) -> Product:
        self._items[product.id] = product
        return product

    def delete(self, product_id: str) -> None:
        self._items.pop(product_id, None)

    def list_all(self) -> list[Product]:
        return list(self._items.values())

    def list_by_vendor(self, vendor_id: str) -> list[Product]:
        return [p for p in self._items.values() if p.vendor_id == vendor_id]


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self._items: dict[str, Order] = {}

    def create(self, order: Order) -> Order:
        self._items[order.id] = order
        return order

    def get_by_id(self, order_id: str) -> Optional[Order]:
        return self._items.get(order_id)

    def update(self, order: Order) -> Order:
        self._items[order.id] = order
        return order

    def list_by_customer(self, customer_id: str) -> list[Order]:
        return [o for o in self._items.values() if o.customer_id == customer_id]

    def list_by_vendor(self, vendor_id: str) -> list[Order]:
        return [o for o in self._items.values() if o.vendor_id == vendor_id]

    def list_all(self) -> list[Order]:
        return list(self._items.values())
