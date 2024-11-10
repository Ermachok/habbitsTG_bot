from fastapi import FastAPI, Request
import telebot

bot = telebot.TeleBot("7261139127:AAGWPFn-O50s19v7ioZKQoBDnIOITTTzHdM")

app = FastAPI()
bot.remove_webhook()
bot.set_webhook(url='')


@app.post("/webhook")
async def webhook(request: Request):
    update = await request.json()
    bot.process_new_updates([telebot.types.Update.de_json(update)])
    return {"status": "ok"}

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    print(message.text)
    bot.reply_to(message, "Привет! Как я могу помочь?")


