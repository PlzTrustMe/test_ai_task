from fastapi import APIRouter
from starlette.responses import RedirectResponse

router = APIRouter()


@router.get(path="/", response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url="/docs")
