import os
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from api.routes import router as api_router
from bot.bot import bot

app = FastAPI()

app.include_router(api_router)
bot.remove_webhook()
bot.set_webhook(url=os.getenv("NGROK_URL"))
