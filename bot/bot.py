from telebot import TeleBot
from redis import StrictRedis
from config import Config
import requests

bot = TeleBot(Config.BOT_TOKEN)

redis_client = StrictRedis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT,
    password=Config.REDIS_PASSWORD,
    decode_responses=True,
)


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Hello!")


@bot.message_handler(commands=["create_new_user"])
def create_new_user(message):
    bot.reply_to(message, "Nice! Send me your login and password divided by ';'")
    redis_client.set(f"user:{message.chat.id}:state", "waiting_for_login_password")


@bot.message_handler(
    func=lambda message: redis_client.get(f"user:{message.chat.id}:state")
    == "waiting_for_login_password"
)
def process_login_password(message):
    """Process login and password"""
    try:

        login, password = message.text.split(";")
        redis_client.delete(f"user:{message.chat.id}:state")
        response = requests.post(
            f"{Config.NGROK_URL}/create_user",
            json={"login": login, "password": password},
        )

        if response.status_code == 200:
            bot.reply_to(message, "User created successfully!")
        else:
            bot.reply_to(message, f"Failed to create user: {response.text}")

    except ValueError:
        bot.reply_to(
            message, "Invalid format. Please send login and password divided by ';'."
        )
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")
