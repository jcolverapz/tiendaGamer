import time
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

TOKEN = '1650639438:AAFgE3DIx0qzmAvBJc8Wu5acXUVoFSHE_vY'
#bot = telebot.TeleBot(TOKEN)

bot = telepot.Bot(TOKEN)
print('Listening ...')
#token = <token>
user = '1204307512' # user id

keyboard=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="First Button")]])
bot.sendMessage(user, 'Use custom keyboard', reply_markup=keyboard)

time.sleep(4)

#bot.sendMessage(user, 'Deleting keyboard', reply_markup=ReplyKeyboardRemove())