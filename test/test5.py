import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from telethon import TelegramClient, events
import request
import os

bot= TelegramClient('botjjjjj',165251,'1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0').start(bot_token='1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0)

TOKEN= '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0'
 
def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('hello')
    update.message.reply_text('')
#update.message.reply_text(f'Your {text.lower()}? Yes, I would love to hear about that!')
def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

updater= Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()

print("Hecho")
updater.idle()