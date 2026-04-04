from fastapi import APIRouter

from app.presentation.api.v1.routers import auth, health, orders, products, vendors

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(auth.router)
api_router.include_router(vendors.router)
api_router.include_router(products.router)
api_router.include_router(orders.router)
