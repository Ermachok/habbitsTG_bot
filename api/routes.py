from fastapi import APIRouter, Request
from bot.bot import bot
import telebot

router = APIRouter(prefix="/webhook")

@router.post('')
async def webhook(request: Request):
    update = await request.json()
    bot.process_new_updates([telebot.types.Update.de_json(update)])
    return {"status": "ok"}


@router.post("/check")
async def check(request: Request):
    data = await request.json()
    print(data)
    return {"status": "ok"}