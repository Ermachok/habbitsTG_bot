import telebot
import bcrypt

from bot.bot import bot
from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from api.db import async_session
from api.schemas.schemas import UserCreate, UserResponse
from api.models.models import User


router = APIRouter(prefix="/webhook")

@router.post('')
async def webhook(request: Request):
    update = await request.json()
    bot.process_new_updates([telebot.types.Update.de_json(update)])
    return {"status": "ok"}

async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session


@router.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):

    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

    db_user = User(
        name=user.name,
        telegram_id=user.telegram_id,
        is_active=user.is_active,
        password=hashed_password,
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


@router.post("/check")
async def check(request: Request):
    data = await request.json()
    return {"status": "ok"}