from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from main_app.api.user import router as user_router
from main_app.utils import get_logger

logger = get_logger(__name__)

app = FastAPI(title="User API", version="0.3")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=[],
)

app.include_router(user_router)


@app.on_event("startup")
async def startup_event():
    logger.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")

