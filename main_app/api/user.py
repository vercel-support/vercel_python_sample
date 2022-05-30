import os

from fastapi import APIRouter, Depends, status
from main_app.utils import get_logger

router = APIRouter(prefix="/v1/user")

logger = get_logger(__name__)

@router.get("/token/{token}")
async def find_user_token(
    token: str):
    logger.info(f"return user per tokenn {token}")

