import logging

from fastapi import FastAPI

from .base import router as base_router
from .text import router as text_router


def include_routers(app: FastAPI) -> None:
    app.include_router(base_router)
    app.include_router(text_router)
    logging.info("Routers was included.")


__all__ = [
    "include_routers"
]
