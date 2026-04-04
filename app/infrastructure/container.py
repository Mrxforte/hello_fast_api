from __future__ import annotations

from app.domain.entities.models import Role, User
from app.domain.services.auth_service import AuthService
from app.infrastructure.repositories.in_memory import (
    InMemoryOrderRepository,
    InMemoryProductRepository,
    InMemoryUserRepository,
    InMemoryVendorRepository,
)
from app.infrastructure.security.config import SecuritySettings


class Container:
    def __init__(self):
        self.settings = SecuritySettings()
        self.auth_service = AuthService(
            secret_key=self.settings.secret_key,
            algorithm=self.settings.algorithm,
            token_minutes=self.settings.token_minutes,
        )
        self.user_repo = InMemoryUserRepository()
        self.vendor_repo = InMemoryVendorRepository()
        self.product_repo = InMemoryProductRepository()
        self.order_repo = InMemoryOrderRepository()
        self._seed_admin_user()

    def _seed_admin_user(self) -> None:
        if self.user_repo.get_by_email("admin@example.com"):
            return
        admin = User(
            email="admin@example.com",
            full_name="System Admin",
            password_hash=self.auth_service.hash_password("Admin123!"),
            role=Role.ADMIN,
        )
        self.user_repo.create(admin)


container = Container()
