import logging, os
from telegram.ext import (
    Updater,
    CommandHandler,

)
from dotenv import load_dotenv

load_dotenv(".env")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)
counter = 0


def start(update, context):
    try:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Hello {update.effective_chat.username}!, You can use /quote command to get a quote",
        )
    except Exception as ex:
        print(ex)


def callback_quote(context):
    try:
        chat_id = context.job.context
        print(chat_id)
        context.bot.send_message(chat_id = chat_id, text= "Yeah just testing it!")
    except Exception as ex:
        print(ex)

def get(update, context):
    try:
        context.job_queue.run_repeating(callback_quote, interval = 5, first = 30,
    context = update.message.chat_id)
    except Exception as ex:
        print(ex)

def callback_quote(context):
    try:
        chat_id = context.job.context
        print(chat_id)
        context.bot.send_message(chat_id = chat_id, text= "Yeah just testing it!")
    except Exception as ex:
        print(ex)

def quote(update, context):
    global counter
    try:
        quotes = [
            "Be yourself; everyone else is already taken.",
            "So many books, so little time",
            "A room without books is like a body without a soul.",
        ]
        if update.effective_message.text == "/quote":
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=quotes[counter]
            )
            counter += 1
        else:
            counter = 0
    except Exception as ex:
        print(ex)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('caused error "%s"', context.error)


def main():
    """Start the bot."""
    updater = Updater(os.getenv("TOKEN"), use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("quote", quote))
    dp.add_handler(CommandHandler("get", get))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    logger.info("Starting Bot!!")
    main()
