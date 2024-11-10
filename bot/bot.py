import telebot
import os
import requests

TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = os.getenv("NGROK_URL")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_message(message):
    bot.reply_to(message, "Привет! Как я могу помочь?")


@bot.message_handler(commands=['new_habit'])
def check(message):
    bot.reply_to(message, "New command worked")
    response = requests.post(f"{BASE_URL}/check", json={"name": message.text})
    print(response)
