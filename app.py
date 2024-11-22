import threading
from fastapi import FastAPI
from contextlib import asynccontextmanager


from api.routes import router as api_router
from bot.bot import bot
from config import Config


def start_bot():
    """Start the Telegram bot in a separate thread"""
    bot.remove_webhook()
    bot.set_webhook(url=Config.NGROK_URL)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager to handle startup and shutdown"""
    thread = threading.Thread(target=start_bot, daemon=True)
    thread.start()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)
