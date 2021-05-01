import telethon
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
from telethon.tl.types import ChannelParticipantsKicked
from telethon.tl.types import ChannelParticipantsRecent
#from telethon.tl.types import ChannelAdminLogEventAction
from telethon.tl.types import ChannelAdminLogEventActionParticipantJoin
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import UpdateUserStatus
from telethon.tl.functions.messages import StartBotRequest
import asyncio
from datetime import datetime
import time
import typing
from contacts import agregar, buscar, actualizar, tipo, datos, fecha
from telegram.ext import (Updater,CommandHandler,CallbackQueryHandler,PollAnswerHandler,
PollHandler, MessageHandler,Filters,) 
import sys
#import telebot
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton 
from telegram.error import (TelegramError, Unauthorized, BadRequest, 
                            TimedOut, ChatMigrated, NetworkError)
#import SafeScheduler
from chatbot1 import Enviar
import sched
import schedule
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.blocking import BlockingScheduler


api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@micanaljc' 
################################################
#      Create the client and connect 
#client.connect() # logining and connecting to Telegram servers
client = TelegramClient("session", api_id, api_hash) #.start(bot_token=TOKEN)  
client.start()
print('Starting...')

async def mensajes(arg1, arg2):
     
    msj1= " Hola @" + str(arg1)+ " cómo estás? \n" \
    "Te escribo para agradecerte porque la verdad ya nos compraste varias veces y estamos re contentos! 😁 \n" \
    "Aprovecho también para decirte que siempre nos gusta escuchar opiniones de nuestros clientes. Así que, si podemos ayudarte a mejorar y crecer en tu negocio, ó si tenes algún comentario para hacernos, SON MÁS QUE BIENVENIDOS! \n" \
    "Nuestra idea es siempre mejorar, así que cualquier sugerencia que tengas para darnos, siempre vienen bien. Y si necesitas una mano, también estamos para ayudarte! 🤝🏻 \n" \
    "¡Gracias otra vez! 😎"

    msj2= "Hola @" + str(arg1)+ " cómo estás? \n" \
    "Te escribo porque estamos lanzando algunas ofertas y sólo le llegan a las personas que nos tienen agendados 😕 \n" \
    "Quería saber si seguís con el emprendimiento de los juegos, porque las ofertas están buenas y otros clientes están vendiendo muy bien." 

    msj3=" Hola @" + str(arg1)+ ", ¿cómo estás? 😁 \n" \
    "Te escribo porque nos habías consultado por el negocio de los juegos y nos gustaría darte una mano.\n" \
    "Quería saber si seguías interesado, porque justo estamos lanzando varias OFERTAS y quizás te sirvan para poder empezar a vender.\n" \
    "Todos los juegos que están en oferta los vamos promocionando en listas de difusión. Si te interesa,  agendanos así aprovechas los mejores precios 😎\n" \
    "Si necesitas ayuda para arrancar o no sabes bien por dónde empezar, nosotros te ayudamos! Somos un equipo de varias personas que empezó desde abajo y la verdad nos gusta mucho poder dar una mano a los que están empezando.\n" \
    "Escribinos cuando gustes! 😌"
    
    if arg2==1:
        msj=msj1
    elif arg2==2:
        msj=msj2
    else:
        msj=msj3

    return(msj)
    
global users

TOKEN = '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0'
bot = telepot.Bot(TOKEN)
#bot = telebot.TeleBot(TOKEN)


async def job():
    misdatos= datos()
    for i in misdatos:
        print(i)
        miid = i.get('phone')
        if miid!=None:
            try:
                await client.send_message(miid, 'msj de prueba')
            except:
                "An Exception"
'''
    #print(str(datetime.now()))
    #await client.send_message("MessifansGroup", "Hi!")

#x = datetime.datetime(2018, 9, 15)
#mistr = '04/29/2021 16:54:00'
#str=str(sh.worksheet("mensajes").cell(1, 6).value)
#date_object = datetime.strptime(str, '%m/%d/%y')
#date_object = datetime.strptime(str, '%m/%d/%y %H:%M:%S')
#midate = sh.worksheet("mensajes").cell(1, 6).value
#x = datetime.date(midate)
#x = datetime.datetime(2018, 9, 15)

print(x.strftime("%b %d %Y %H:%M:%S"))
'''
scheduler = AsyncIOScheduler()
scheduler.add_job(job, 'date', run_date='2021-05-01 00:18:00')
scheduler.start()

'''
@sched.scheduled_job('date', run_date=mifecha)
async def start_job():
    print('Schedule job')
 
#job = scheduler.add_job(tick, 'interval', seconds=3600
#from apscheduler.schedulers.blocking import BlockingScheduler
#global habilita
#global count, scheduler
'''
loop = asyncio.get_event_loop()
loop.run_forever()