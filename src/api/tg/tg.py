import asyncio
from asyncio import Task
from typing import Any

from aiogram.methods.base import TelegramType, TelegramMethod
from aiogram.types import Update
from fastapi.responses import ORJSONResponse
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.api.tg.router import router
from src.bg_tasks import background_tasks
from src.bot import get_dp, get_bot


@router.post("/home")
async def home_post(
    request: Request,
    # session: AsyncSession = Depends(get_db),
) -> JSONResponse:
    a = 1
    data = await request.json()
    update = Update(**data)
    dp = get_dp()

    task: Task[TelegramMethod[Any] | None] = asyncio.create_task(dp.feed_webhook_update(get_bot(), update))
    background_tasks.add(task)
    task.add_done_callback(background_tasks.discard)

    return ORJSONResponse({"message": "Hello"})
