from fastapi import FastAPI

from app.presentation.api.v1.api import api_router


app = FastAPI(
    title="Eshop API",
    description="FastAPI clean architecture backend with auth, vendors, products, and orders",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api/v1")