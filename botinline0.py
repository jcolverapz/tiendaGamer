import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.utils.helpers import escape_markdown

# Configurar logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger()

#Solicitar Token
TOKEN='1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0'

def start(update, context) :
    logger.info(f"El usuario {update.effective_user['username']}, ha iniciado una conversacion")
    name = update.effective_user['first_name']
    """Send a message when the command /start is issued."""
    update.message.reply_text("Hi! {name}" )

def echo(update, context):
    user_id= update.effective_user['id']
    logger.info(f"El usuario {update.effective_user['username']}, ha enviado un mensaje de texto")
    text=update.message.text
    context.bot.sendMessage(
        chat_id= user_id,
        parse_mode="MarkdownV2",
        text=f"Escribiste:\n_{text}_"
    )
    


if __name__ == '__main__':
    #Obtenemos informacion de nuestro bot
    mybot = telegram.Bot(token=TOKEN)
    print(mybot.getMe())

#Enlazamos nuestro updater con nuestro bot
updater = Updater(mybot.token, use_context= True)

#Creamos un despachador
dp= updater.dispatcher

#Creamos los manejadores
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, echo))

# Start the Bot
updater.start_polling()
print("Bot iniciado")
# Block until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.

#Permite finalizar el bot con Ctrl+C
updater.idle()


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

   