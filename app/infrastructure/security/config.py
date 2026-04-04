from pydantic import BaseModel


class SecuritySettings(BaseModel):
    secret_key: str = "change_this_secret_in_production"
    algorithm: str = "HS256"
    token_minutes: int = 60
