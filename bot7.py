import telepot
from telepot.loop import MessageLoop
import time
from pprint import pprint
TOKEN = '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0' 
bot = telepot.Bot(TOKEN)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    send1 = bot.sendMessage(chat_id,'whats your name?')
    
    response = bot.getUpdates()
    print(response)
    if send1:
        text1 = msg['text']
        print(text1)


MessageLoop(bot,handle).run_as_thread()
while 1:
    time.sleep(1)
