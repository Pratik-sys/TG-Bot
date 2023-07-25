import os, logging, requests
import telebot
from dotenv import load_dotenv

load_dotenv(".env")
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)
BOT_TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

def fetchword():
    response = requests.get(os.getenv("URL"))
    return response

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Hello {message.from_user.username}")

def main():
    bot.infinity_polling()

if __name__ == "__main__":
    logger.info("Starting Bot!!")
    main()