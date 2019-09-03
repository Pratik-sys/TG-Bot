from telegram.ext import Updater, CommandHandler
import os
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="hello")

def main ():
    updater = Updater(os.environ.get('TOKEN'))
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()

