from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup
from telegram.ext import MessageHandler, Filters
import json
 
TOKEN = '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0' 

#bot = telebot.TeleBot(TOKEN) 

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
channel = '@micanaljc'
################################################
#      Create the client and connect
#client = TelegramClient('newsession', api_id, api_hash)
#client.start()

CHAT_ID = 1204307512 

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def tbot_get_location_n_contact():
    """
    Request for User Contact and Location information.
    """
    location_keyboard = KeyboardButton(text="Share My Location", request_location=True)
    contact_keyboard = KeyboardButton(text="Share My Contact", request_contact=True)
    custom_keyboard = [[ location_keyboard, contact_keyboard ]]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True, resize_keyboard=True)
    return reply_markup

def location(update, context):
    print('Inside location')
    print(update)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Thanks for location information")

def contact(update, context):
    print('Inside Contact')
    print(update)
    print('Contact : {0}'.format(update.effective_message.contact))
    print('Phone : {0}'.format(update.effective_message.contact.phone_number))
    context.bot.send_message(chat_id=update.effective_chat.id, text="Thanks for contact information")

def start(update, context):
    print('Inside Start')
    print(update)
    reply_markup = tbot_get_location_n_contact()
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!", reply_markup=reply_markup)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

contact_handler = MessageHandler(Filters.contact, contact)
dispatcher.add_handler(contact_handler)

location_handler = MessageHandler(Filters.location, location)
dispatcher.add_handler(location_handler)

updater.start_polling()