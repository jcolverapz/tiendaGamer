from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
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
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telethon.tl.functions.messages import StartBotRequest
#from telethon.tl.types import ChannelAdminLogEventAction
import asyncio
from datetime import datetime
import time

from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    PollAnswerHandler,
    PollHandler,
    MessageHandler,
    Filters,
)

import telebot

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@micanaljc'
offset = 0
limit = 100
all_participants = []
users = []
################################################
#      Create the client and connect
client = TelegramClient('newsession', api_id, api_hash)  # feel free to edit %sessionname% as you want
#client.connect() # logining and connecting to Telegram servers
client.start()
 
global lista1
lista1=[]

@client.on(events.UserUpdate)
async def handler(event):
    global lista1

    if event.online:
        print("Evento")

        lista2 = []
        participants2 = await client(GetParticipantsRequest(channel,ChannelParticipantsSearch(''),0,0,hash=0))
        new_users = []
        new_users.clear()
        
        for u in participants2.users:

            lista2.append([u.id, u.username])

        for us in lista2:
            if us[0] in lista1:
               a=1
            else:
                new_users.append(us)
        
        for i in new_users:
            print('id:' + str(i[0]) , 'user: '+ str(i[1]))
           
            mensaje="➡️ Hola ¿Cómo estás?  @"  + str(i[1]) + " , Bienvenido a NEGOCIO GAMER, 😁 \n"  \
                    "➡️ Te comento brevemente ,somos un equipo de 8 personas, en donde nos vamos a encargar de brindarte una excelente atención y asesoramiento para que puedas realizar tus ventas de la mejor manera 😉 \n"  \
                    "➡️ Nos dedicamos a la venta de juegos de Playstation 4 y también de Giftcard. \n" \
                    "➡️ Nuestros productos son originales, por lo que ofrecemos garantía de por vida por cada uno de ellos. \n" \
                    "➡️ Contamos con Servicio técnico PROPIO , para resolver cualquier duda o inconveniente que tengas a la brevedad. \n" \
                    "➡️ Contamos con más de 1 año de experiencia en el rubro y trabajamos con más de 1500 revendedores."
            
           
            #await client.send_message('@pruebastienda',mensaje)
            await client.send_message(i[0],mensaje)
            #await client.send_message(i, mensaje)
            
           

            TOKEN = '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0'
            #bot = telebot.TeleBot(TOKEN)
            #bot.send_message(1496283722, 'mensaje de prueba')

            bot = telepot.Bot(TOKEN)
            bot.sendMessage(1496283722,'mensaje de prueba')
            #print("Enviar msj " + str(i[1]))
            if i[0]!=  1686414837:
                try:
                    print("Enviado")
                    #bot.send_message(1204307512, 'mensaje de prueba')
                except:
                    print("An exception occurred")
                
              
            new_users.remove(i)
            lista1.append(i[0])
           
        print('finalizo el evento')

# content of the automatic reply

if __name__ == '__main__':
    
    print(time.asctime(), '-', 'Auto-replying...')
    #client.connect() # logining and connecting to Telegram servers
    client.start()
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')


loop = asyncio.get_event_loop()
