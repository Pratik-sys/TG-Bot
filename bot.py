import os, logging, time, threading, schedule
import telebot
from dotenv import load_dotenv
from RandomWord import getRandomWord

load_dotenv(".env")
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
)
logger = logging.getLogger(__name__)
BOT_TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Hello *{message.from_user.username}* use `/set` command to set the timer", parse_mode='MARKDOWN')

@bot.message_handler(commands=['set'])
def set_timer(message):
    user_input  = message.text.split()
    if(len(user_input) > 1 and user_input[1].isdigit()):
        shdl = int(user_input[1])
        # schedule.every.day.at(shdl).do(send_word, message.chat.id).tag(message.chat.id)
        schedule.every(shdl).seconds.do(send_word, message.chat.id).tag(message.chat.id)
        bot.reply_to(message, f"Timer has been set to {shdl} seconds")
        logger.info(f"Timer has been set to {shdl}s")
    else:
        bot.reply_to(message, 'Usage: /set <time>')

@bot.message_handler(commands=['unset'])
def unset_timer(message):
    joblist  = schedule.get_jobs()
    if(joblist):
        schedule.clear(message.chat.id)
        bot.reply_to(message, "Schedule is been cleared from the queue")
        logger.info(f"Schedule is removed from queue for user -  {message.from_user.username} ")
    else:
        bot.reply_to(message, "There is no schedule to clear from the queue")

@bot.message_handler(commands=['listjobs'])
def getjoblist(message):
    joblist  = schedule.get_jobs()
    if(joblist):
        bot.reply_to(message, schedule.get_jobs())
        logger.info(f"list of schedule for the user -  {message.from_user.username} are {joblist} ")
    else:
        bot.reply_to(message, "No schedule is set so far, please use `/set <time>` command to set timer")
        logger.info(f"No Shcedule found for user -  {message.from_user.username}  ")

                   
def send_word(message):
    word = getRandomWord()
    dictlink = f"https://www.google.com/search?q={word}"
    bot.send_message(message, f"Checkout for new word today is *{word}* \n\n please navigate to given link to checkout the defintion {dictlink}", parse_mode='MARKDOWN')

if __name__ == '__main__':
    logger.info("Starting Bot!!")
    threading.Thread(target=bot.infinity_polling, name='bot_infinity_polling', daemon=True).start()
    while True:
        schedule.run_pending()
        time.sleep(1)