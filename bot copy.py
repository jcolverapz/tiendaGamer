from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.types import InputChannel
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import User
from telethon.tl.types import ChannelParticipant
from telethon.tl.types import ChannelParticipantsKicked # import type to use as filter
from telethon.tl.types import ChannelParticipantsRecent
from telethon.tl.types import ChannelAdminLogEventActionParticipantJoin
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import UpdateUserStatus
from telethon.tl.functions.messages import StartBotRequest

#from telepot import telebot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

#from telethon.tl.types import ChannelAdminLogEventAction
import asyncio
from datetime import datetime
import time
import typing
from contacts import miscontactos, buscar
from telegram.ext import (Updater,CommandHandler,CallbackQueryHandler,PollAnswerHandler,
PollHandler, MessageHandler,Filters,) 
import sys
from chatbot1 import Enviar

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@micanaljc' 
################################################
#      Create the client and connect
#client = TelegramClient('newsession', api_id, api_hash)  # feel free to edit %sessionname% as you want
#client.connect() # logining and connecting to Telegram servers
client = TelegramClient("session", api_id, api_hash) #.start(bot_token=TOKEN)
client.start()
 
global users

TOKEN = '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0'
bot = telepot.TeleBot(TOKEN) 
#bot.send_message(1204307512, 'Use inline keyboard')
Enviar()

#@client.on(events.UserUpdate)
#async def handler(event):
    #miid=event.user_id
    global lista1

    if event.online:
        print("Evento")
        
        #print('lista1:' + str(lista1))
        lista1=buscar()
        lista2 = []
        participants2 = await client(GetParticipantsRequest(channel,ChannelParticipantsSearch(''),0,0,hash=0))
        
        new_users = []
        new_users.clear()
        #print(new_users)
         #print('u: ' + str(u.phone))
            #if u.username is None :
	           # u.username = []
           # fullstring = u.username
             
            #if substring in fullstring:
                   # print ("Found! ")
           # else:
                    #print ("Not found!" + u.username)
            #with TelegramClient("new", api_id, api_hash) as client:
       

        for u in participants2.users:
           
            user_id = u.id
            first_name = u.first_name
            last_name = u.last_name
            username = u.username
            phone = u.phone
            mutual=u.mutual_contact
            full  = await client(functions.users.GetFullUserRequest(id=  user_id ))
            phone = full.user.phone
            #print(full)

            lista2.append([user_id, first_name, last_name, username, phone, mutual])
            #print(phone)
            #print('lista2:' + str(lista2[0]) , str(lista2[1]))
        
        for us in lista2:

            if us[0] in lista1:
               a=1
            else:
                #print(us[0])
               # new_users.append(us)
               # miscontactos(us)
                await client.send_message(us[0], "t.me/dante_dog_bot")
                #bot.send_message(1204307512, 'mensaje de prueba')
                print(us[0])
                
        for i in new_users:
            
            lista1.append(us)
            new_users.remove(i)
           
             
            """
            mensaje="➡️ Hola ¿Cómo estás?  @"  + str(i[1]) + " , Bienvenido a NEGOCIO GAMER, 😁 \n"  \
                    "➡️ Te comento brevemente ,somos un equipo de 8 personas, en donde nos vamos a encargar de brindarte una excelente atención y asesoramiento para que puedas realizar tus ventas de la mejor manera 😉 \n"  \
                    "➡️ Nos dedicamos a la venta de juegos de Playstation 4 y también de Giftcard. \n" \
                    "➡️ Nuestros productos son originales, por lo que ofrecemos garantía de por vida por cada uno de ellos. \n" \
                    "➡️ Contamos con Servicio técnico PROPIO , para resolver cualquier duda o inconveniente que tengas a la brevedad. \n" \
                    "➡️ Contamos con más de 1 año de experiencia en el rubro y trabajamos con más de 1500 revendedores."
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Press me', callback_data='press')],
               ])
            """
            """
            await client.sendMessage(i[0], reply_markup=keyboard)
            #await client.send_message('@micanaljc',reply_markup=keyboard) #Esto da Error
#            await client.send_message(i[0],mensaje)
            #phone: typing.Callable[[], str] = lambda: input('Please enter your phone (or bot token): '),
            #print(phone)
            #await client.send_message('@dante_dog_bot','/start')
            """           
            #request = StartBotRequest("dante_dog_bot", "dante_dog_bot", "params_string")
            #result = await client(request)
            #print("Enviar msj " + str(i[1]))
            """
            if us[0]!=  1686414837:
                #try:
                   # print("Enviado")
                    bot.send_message(1511413607, 'mensaje de prueba')
                except:
                    print("An exception occurred")
              
             print('mensaje enviado a ' + str(i[0]))
            """
           
               # main()
        #lista1 = lista2
       # print('lista1:' + str(lista1))
        print('finalizo el evento')

# content of the automatic reply
#message= "@dante_dog_bot"


#message=" Te comento como nos manejamos : \n"   \
#"▪️ Primero que nada tene en claro que no necesitas inversion, simplemente ofreces los juegos disponibles que tenemos , cuando vendes, nos abonas, y a los 30 minutos que impacte el pago te enviamos el juego a tu mail. \n"   \
#"▪️ En el mail te llega el juego junto al instructivo de instalacion y un video tutorial para que tu cliente se pueda guiar mientras lo instala. \n"   \
#"▪️ Todo nuestro stock disponible con el respectivo precio lo podes ver en tiempo real en el link de nuestro excel."

if __name__ == '__main__':
    # Create the client and connect
    # use sequential_updates=True to respond to messages one at a time
    #client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)

    @client.on(events.NewMessage(pattern='(?i)mala atención.+'))
    @client.on(events.NewMessage(pattern='(?i)hello.+'))
    async def handler(event):
        # Respond whenever someone says "Hello" and something else
        await event.reply('Te pido disculpas!')

    @client.on(events.NewMessage(outgoing=True, pattern='nada'))
    async def handler(event):
        # Say "!pong" whenever you send "!ping", then delete both messages
        m = await event.respond('!Ok')
        await asyncio.sleep(5)
        await client.delete_messages(event.chat_id, [event.id, m.id])

    

    print(time.asctime(), '-', 'Auto-replying...')

"""
    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        #await client.send_message(1511413607, 'mensaje de prueba')

       # if event.is_private:  # only auto-reply to private chats
           # from_ = await event.client.get_entity(event.from_id)  # this lookup will be cached by telethon
            #print(event.message)
            
           # if not from_.bot:  # don't auto-reply to bots
                #bot.send_message(1511413607, 'mensaje de prueba')
           
                #print(time.asctime(), '-', event.message)  # optionally log time and message
            #time.sleep(1)  # pause for 1 second to rate-limit automatic replies
            #await event.respond("message")

"""
    
    #client.connect() # logining and connecting to Telegram servers
client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Stopped!')



loop = asyncio.get_event_loop()
#def main():
#    enlistar()
#async def enlistar():
    # global all_participants
#    print(' lista1:'  + str(main.lista1))
#async def enviar():


########### codigo
'''
import asyncio
async def work():
    while True:
        await asyncio.sleep(10)
        print("Task Executed")

loop = asyncio.get_event_loop()

try:
    asyncio.ensure_future(work())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()
'''
