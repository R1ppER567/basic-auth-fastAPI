from typing import Any

from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from src.dependencies import auth_dev


router = APIRouter(include_in_schema=False, dependencies=[Depends(auth_dev)])


@router.get('/docs')
async def custom_swagger(request: Request) -> HTMLResponse:
    return get_swagger_ui_html(
        openapi_url=str(request.url_for('custom_openapi')),
        title='Docs'
    )


@router.get('/openapi.json')
async def custom_openapi(request: Request) -> dict[str, Any]:
    return get_openapi(
        title=request.app.title,
        version=request.app.version,
        routes=request.app.routes
    )
