from telegram.ext import Updater, CommandHandler

def start(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="hello")

def main ():
    updater = Updater('TOKEN')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()

