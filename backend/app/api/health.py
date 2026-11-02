from fastapi import APIRouter

from app.core.config import get_settings

router = APIRouter(tags=["system"])


@router.get("/health")
def health() -> dict:
    s = get_settings()
    return {"status": "ok", "currency": s.default_currency, "timezone": s.default_timezone}
