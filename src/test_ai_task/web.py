import logging

import uvicorn
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from test_ai_task.bootstrap.di import setup_http_di
from test_ai_task.presentation.endpoints import include_routers

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

app = FastAPI(title="Summarize text")

logging.info("App was created.")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.info("Initialized app middlewares.")

include_routers(app)

setup_dishka(setup_http_di(), app)
logging.info("Dishka was setup.")


if __name__ == "__main__":
    uvicorn.run(
        app="__main__:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
