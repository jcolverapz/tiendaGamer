import telepot
from telepot.loop import MessageLoop
import time
TOKEN = '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0' 

bot = telepot.Bot(TOKEN)

def Enviar():
    print('Enviando...')
    try:
        bot.sendMessage(1496283722,'whats your name?')
    except:
        print('No es posible enviar msj')
        
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Contestando...')
    send1 = bot.sendMessage(chat_id,'whats your name?')
    if send1:
        text1 = msg['text']
        print(text1)

def main():
    """Start the bot."""
    Enviar()
    #bot.run_until_disconnected()

if __name__ == '__main__':
    main()

#MessageLoop(bot,handle).run_as_thread()
#while 1:
    #time.sleep(1)

