from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class VendorCreateRequest(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    description: str = Field(min_length=3, max_length=500)


class VendorResponse(BaseModel):
    id: str
    owner_user_id: str
    name: str
    description: str
    created_at: datetime
