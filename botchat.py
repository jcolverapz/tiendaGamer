from telethon import TelegramClient, events
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    PollAnswerHandler,
    PollHandler,
    MessageHandler,
    Filters,
)
import telebot # Importamos las librería
import time
api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
TOKEN = '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0' 
#bot = telebot.TeleBot(TOKEN) 
bot = TelegramClient("bot", api_id, api_hash).start(bot_token=TOKEN)

msj0= "Hola, como estas"  
msj1= "Uh qué  pena! ¡Bueno te deseamos mucha suerte \n" \
    "en lo que emprendas y si tenes ganas de volver a probar con el negocio gamer, contá con nosotros para  \n" \
    "lo que necesites que te vamos a ayudar! 😄"

#@bot.on(events.NewMessage(pattern='(?i)mala atencion|mala atención'))
#@bot.on(events.NewMessage(pattern='(?i)mala atencion'))
#@bot.on(events.NewMessage(pattern=r'hi (\w+)!'))
@bot.on(events.NewMessage(pattern='(?i).*hi|hello'))
async def my_event_handler(event):
    #print(event.stringify())
    print('se uso el bot')
    time.sleep(1) 
    await bot.send_message(event.chat.id, msj0)
    #await event.respond(message)

@bot.on(events.NewMessage(pattern='(?i).*mala *atenci.n'))
async def my_event_handler(event):
    #print(event.stringify())
    print('se uso el bot')
    time.sleep(1) 
    await bot.send_message(event.chat.id, msj1)
    #await event.respond(message)


'''
@bot.on(events.NewMessage(pattern='(?i)hi|hello'))
async def handler(event):
    await event.respond('Hey!')

@bot.message_handler(func=lambda message: message.text =='mala atencion|mala atención')
def command_text_hi(message):
    bot.send_message(message.chat.id,msj)

@bot.message_handler(func=lambda message: message.text =='mala atención')
def command_text_hi(message):
    bot.send_message(message.chat.id,msj)

    #bot.reply_to(message, "Howdy, how are you doing?")


'''
#def send_welcome(message):
	#bot.reply_to(message, "Howdy, how are you doing?")
 
def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()

#bot.send_message(1204307512, 'hola') # Ejemplo tb.send_message('109556849', 'Hola mundo!')
#@bot.on('message') 
#async def echo(event):
#print('Respondio algo')
'''
#@bot.message_handler(events.NewMessage(pattern='/start'))
#message.new_chat_member.username
#@bot.message_handler(commands=['start', 'help'])
#@bot.message_handler(message=['hi', 'hola'])

#updater = Updater("1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0", use_context=True)
#updater.start_polling()
'''

'''
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    #bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, 'test')
    #await bot.send_message(1204307512, message.text)
'''
'''
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    #bot.reply_to("👍", message.text)
    bot.send_message(message.chat.id, "👍")
    #await bot.send_message(1204307512, message.text)


@bot.message_handler(func=lambda message: message.text == "hi")
async def command_text_hi(message):
    await bot.send_message(message.chat.id, "I love you too!")

            await client.send_message(us[0], "Dar click en: \n  \
                    "t.me/dante_dog_bot")     
            print(us[0])
''' 