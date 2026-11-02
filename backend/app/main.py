from fastapi import FastAPI

from app.api import health

app = FastAPI(
    title="Family ERP",
    description="Семейная учетно-аналитическая система",
    version="0.1.0",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

app.include_router(health.router, prefix="/api")
