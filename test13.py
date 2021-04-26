import sys
import time
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from telethon.tl.functions.users import GetFullUserRequest

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat Message:', content_type, chat_type, chat_id)
    full = client(GetFullUserRequest(user))
    #users.getFullUser

    if content_type == 'text':
        if msg['text'] == '/key':
            print('key...')
           
            location_keyboard = KeyboardButton(text="send_location",  request_location=True)           #creating location button object
            contact_keyboard = KeyboardButton('Share contact', request_contact=True)  #creating contact button object

            custom_keyboard = [[ location_keyboard, contact_keyboard ]] #creating keyboard object
            reply_markup = ReplyKeyboardMarkup(custom_keyboard) 


            bot.sendMessage(1204307512, 'Example', reply_markup=reply_markup)
            #bot.sendMessage(1204307512, 'testing custom keyboard',
                            #reply_markup=ReplyKeyboardMarkup(
                                #keyboard=[
                                   # [KeyboardButton(text="Yes"), KeyboardButton(text="No")]
                                #]
                            #))

 
TOKEN = '1650639438:AAFgE3DIx0qzmAvBJc8Wu5acXUVoFSHE_vY'
#bot = telebot.TeleBot(TOKEN)

#TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
print('Listening ...')
bot.message_loop({'chat': on_chat_message}, run_forever=True)