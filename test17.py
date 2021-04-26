from telethon.sync import TelegramClient
from telethon import functions, types
import telebot
from telethon.tl.functions.messages import StartBotRequest

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@micanaljc'

################################################
#      Create the client and connect
client = TelegramClient('newsession', api_id, api_hash)  # feel free to edit %sessionname% as you want
#client.connect() # logining and connecting to Telegram servers
client.start()

# content of the automatic reply

TOKEN = '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0'
bot = telebot.TeleBot(TOKEN)

with TelegramClient("session", api_id, api_hash) as client:
   """
    result = client(functions.messages.StartBotRequest(
        bot='@dante_dog_bot',
        peer='@dante_dog_bot',
        start_param='/start'
    ))
    print(result.stringify())
"""

request = StartBotRequest("dante_dog_bot", "dante_dog_bot", "params_string")
result =  client(request)

 
client.run_until_disconnected()