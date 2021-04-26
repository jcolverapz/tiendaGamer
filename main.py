
from telegram.ext import *

print ("Bot started...")

def start_command(update,context):
    update.message.reply_text('Type')

def sample_responses(input_text):
    user_message = str(input_text).lower()

if user_message in ('Hello'):
    return "Hey"

def handle_message(update, context):
    text=str(update.message.text).lower()
    response = R.sample_responses(text)
    update.message.reply_text(response)

def main():
    updater = Updater(keys.API_KEY, use_context=true)
    dp = updater.dispatcher
    update.message.repply_text(response)

    updater.start_polling()
    updater.idle()