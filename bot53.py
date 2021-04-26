import logging
#from config import tgtoken
from telegram.ext import Updater, CommandHandler


api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@micanaljc'
#client = TelegramClient('newsession', api_id, api_hash)

TOKEN = '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0'
#bot = telebot.TeleBot(TOKEN)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def sum(update, context):
    try:
        number1 = int(context.args[0])
        number2 = int(context.args[1])
        result = number1+number2
        update.message.reply_text('The sum is: '+str(result))
    except (IndexError, ValueError):
        update.message.reply_text('There are not enough numbers')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("sum", sum))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()