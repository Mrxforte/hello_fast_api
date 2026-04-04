from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entities.models import Order, Product, User, Vendor


class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, user_id: str) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> list[User]:
        raise NotImplementedError


class VendorRepository(ABC):
    @abstractmethod
    def create(self, vendor: Vendor) -> Vendor:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, vendor_id: str) -> Optional[Vendor]:
        raise NotImplementedError

    @abstractmethod
    def get_by_owner(self, owner_user_id: str) -> Optional[Vendor]:
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> list[Vendor]:
        raise NotImplementedError


class ProductRepository(ABC):
    @abstractmethod
    def create(self, product: Product) -> Product:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, product_id: str) -> Optional[Product]:
        raise NotImplementedError

    @abstractmethod
    def update(self, product: Product) -> Product:
        raise NotImplementedError

    @abstractmethod
    def delete(self, product_id: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> list[Product]:
        raise NotImplementedError

    @abstractmethod
    def list_by_vendor(self, vendor_id: str) -> list[Product]:
        raise NotImplementedError


class OrderRepository(ABC):
    @abstractmethod
    def create(self, order: Order) -> Order:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, order_id: str) -> Optional[Order]:
        raise NotImplementedError

    @abstractmethod
    def update(self, order: Order) -> Order:
        raise NotImplementedError

    @abstractmethod
    def list_by_customer(self, customer_id: str) -> list[Order]:
        raise NotImplementedError

    @abstractmethod
    def list_by_vendor(self, vendor_id: str) -> list[Order]:
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> list[Order]:
        raise NotImplementedError
