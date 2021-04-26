import sys
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardHide, ForceReply
import time

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print ('Chat:', content_type, chat_type, chat_id)
    if content_type != 'text':
        return
    command = msg['text'].lower()

    if command == '/reboot':
        markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Confirm')], [KeyboardButton(text='Cancel')]], one_time_keyboard=True)
        bot.sendMessage(chat_id, 'Reboot?', reply_markup=markup)
    #elif command == 'Confirm':
    ## EXECUTE sudo reboot...
    #else:
        #bot.sendMessage(chat_id, str('Wrong command!'))
TOKEN = '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0'

#TOKEN='xxxxx'
bot = telepot.Bot(TOKEN)
bot.message_loop({'chat': on_chat_message})
while 1:
    time.sleep(10)