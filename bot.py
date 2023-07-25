import os, logging,requests,asyncio, time, threading, schedule
import telebot
from dotenv import load_dotenv

load_dotenv(".env")
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)
BOT_TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

async def fetchword():
    response = requests.get(os.getenv("URL"))
    content = response.json()
    return content.get('word')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Hello {message.from_user.username} use `/set` command to set the timer")

@bot.message_handler(commands=['set'])
def set_timer(message):
    user_input  = message.text.split()
    if(len(user_input) > 1 and user_input[1].isdigit()):
        shdl = int(user_input[1])
        # schedule.every.day.at(shdl).do(send_word, message.chat.id).tag(message.chat.id)
        schedule.every(shdl).seconds.do(send_word, message.chat.id).tag(message.chat.id)
        bot.reply_to(message, f"Timer has been set to {shdl} seconds")

    else:
        bot.reply_to(message, 'Usage: /set <time>')

@bot.message_handler(commands=['unset'])
def unset_timer(message):
    schedule.clear(message.chat.id)
    bot.reply_to(message, "Schedule is been cleared from the queue")

@bot.message_handler(commands=['listjobs'])
def getjoblist(message):
    joblist  = schedule.get_jobs()
    if(joblist):
        bot.reply_to(message, schedule.get_jobs())
    else:
        bot.reply_to(message, "No schedule is set so far, please use `/set <time>` command to set timer")
                   
def send_word(message):
    bot.send_message(message, asyncio.run(fetchword()))

if __name__ == '__main__':
    logger.info("Starting Bot!!")
    threading.Thread(target=bot.infinity_polling, name='bot_infinity_polling', daemon=True).start()
    while True:
        schedule.run_pending()
        time.sleep(1)