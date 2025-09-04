from fastapi import FastAPI

from src.routers import auth, docs
from src.core.settings import settings


app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None
)

if settings.mode == 'DEV':
    app.include_router(docs.router)
app.include_router(auth.router)
