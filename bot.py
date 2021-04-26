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
from contacts import agregar, buscar, actualizar, tipo, datos
from telegram.ext import (Updater,CommandHandler,CallbackQueryHandler,PollAnswerHandler,
PollHandler, MessageHandler,Filters,) 
import sys
#import telebot
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton 
from telegram.error import (TelegramError, Unauthorized, BadRequest, 
                            TimedOut, ChatMigrated, NetworkError)

from chatbot1 import Enviar

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@micanaljc' 
################################################
#      Create the client and connect 
#client.connect() # logining and connecting to Telegram servers
client = TelegramClient("session", api_id, api_hash) #.start(bot_token=TOKEN)  
client.start()
print('Starting Client')


msj5=" Te comento como nos manejamos : \n"   \
"▪️ Primero que nada tene en claro que no necesitas inversion, simplemente ofreces los juegos disponibles que tenemos , cuando vendes, nos abonas, y a los 30 minutos que impacte el pago te enviamos el juego a tu mail. \n"   \
"▪️ En el mail te llega el juego junto al instructivo de instalacion y un video tutorial para que tu cliente se pueda guiar mientras lo instala. \n"   \
"▪️ Todo nuestro stock disponible con el respectivo precio lo podes ver en tiempo real en el link de nuestro excel."

msj6="Bueno eso seria la informacion necesaria que necesitas para poder empezar, acordate que si tenes alguna duda o consulta nos podes decir y te la resolvemos al instante.\n"   \
"Muchas gracias y nuevamente te damos la bienvenida al rubro.😁 \n"   \
"➡️  Si nos mandas una captura de como nos tenes agendados te damos un descuento del 10 '%' en tu primer compra en cualquiera de nuestros juegos en stock 😁"

msj0= "Hola, ¿Cómo estás?. Bienvenido a NEGOCIO GAMER. 😁\n" \
"➡️Te comento brevemente ,somos un equipo de 8 personas, en donde nos vamos a encargar de brindarte una excelente atención y asesoramiento para que puedas realizar tus ventas de la mejor manera 😉.\n" \
"➡️ Nos dedicamos a la venta de juegos de Playstation 4 y también de Giftcard.\n" \
"➡️ Nuestros productos son originales, por lo que ofrecemos garantía de por vida por cada uno de ellos.\n" \
"➡️ Contamos con Servicio técnico PROPIO , para resolver cualquier duda o inconveniente que tengas a la brevedad.\n" \
"➡️ Contamos con más de 1 año de experiencia en el rubro y trabajamos con más de 1500 revendedores."

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
i=1 

async def Enviarmensaje():
   
    global lista1
    #print("BBDD de Sheets...")

    lista1= buscar()
    lista2 = []
    lista2.clear()
    #print("BBDD Telegram...")
    participants2 = await client(GetParticipantsRequest(channel,ChannelParticipantsSearch(''),0,0,hash=0))
    #new_users = []
    #new_users.clear()
    misdatos= datos()
    #print(participants2)
   
    for u in participants2.users:

        user_id = u.id
        first_name = u.first_name
        last_name = u.last_name
        username = u.username
       
        if username==None:
            username="NONE"
        
        #phone = u.phone
        mutual=u.mutual_contact
        
        full  = await client(functions.users.GetFullUserRequest(id=  user_id ))
        phone = full.user.phone
        print('phone:' + str(phone))
        compro="NO"
        # Campo: Compro
        for i in misdatos:
            #print('comprobando...'+ str(i))
            #print(type(i.get('phone')))
           
            print('GET phone:' + str(i.get('phone')))          
            if phone!=None:

                if int(i.get('phone')) == int(phone):
                    print('encontrado:...' + username )
                    compro = i.get('compro')
                    volvio = i.get('volvio')
                    agendo = i.get('agendo')
                    #print('compro: ' + compro)
        
        lista2.append([user_id, first_name, last_name, username, phone, mutual, compro, volvio, agendo])
        #print(lista2)
   
    for us in lista2:   #print('Agregando a sheets...')
        #mitipo=1
       
        if us[3]=="":
            us[3]="NONE"

        if us[6]=="SI" and us[7]=="SI":
            tipo= 1
                
        elif us[6]=="SI" and us[7]=="NO":
            tipo= 2

        else:
            tipo= 3

        msj  = await mensajes(us[3], tipo)
       
        if us[0] in lista1:   #Usuario Existente
            print('user encontrado: ' + str(us[0]))
            #print(us[0], us[4])
            #actualizar(us[3], us[6])
           
        else:
            #Nuevo Usuario
            agregar(us)         
            bienvenido="➡️ Hola ¿Cómo estás?, Bienvenido a NEGOCIO GAMER, 😁 \n" \
            "➡️ Te comento brevemente ,somos un equipo de 8 personas, en donde nos vamos a encargar de brindarte una excelente atención y asesoramiento para que puedas realizar tus ventas de la mejor manera 😉 \n" \
            "➡️ Nos dedicamos a la venta de juegos de Playstation 4 y también de Giftcard. \n" \
            "➡️ Nuestros productos son originales, por lo que ofrecemos garantía de por vida por cada uno de ellos. \n" \
            "➡️ Contamos con Servicio técnico PROPIO , para resolver cualquier duda o inconveniente que tengas a la brevedad. \n" \
            "➡️ Contamos con más de 1 año de experiencia en el rubro y trabajamos con más de 1500 revendedores."
            
            msj4= "➡️ Hola ¿Cómo estás? @" + str(us[3]) + ", Bienvenido a NEGOCIO GAMER, 😁 \n" \
            "➡️ ...para mas informacion, dar clic en el siguiente enlace \n" \
            "t.me/dante_dog_bot"
           
            #await client.send_message(us[0], 'bienvenido')
            #print('Enviando mensaje')
            #await bot.send_message(1496283722, 'Bienvenido')
            #await bot.sendMessage(1496283722,'mensaje de prueba')

            try:
                print('Enviando por bot a:' + str(us[0]))
                await client.send_message('@micanaljc', bienvenido)
                #await bot.send_message(1496283722, msj)
                await bot.sendMessage(us[0],msj)
            
            #except TelegramError:
            except:
                #print('Enviando por user a: '+ str(us[0]))
                print('Excepcion encontrada')
                await client.send_message(us[0], bienvenido)
                await client.send_message(us[0], msj5)
                await client.send_message(us[0], msj6)
            

async def main():
    while True:
        await asyncio.sleep(5)
        try:
            await Enviarmensaje()
            #print("Task Executed")
        except:
            "No se ejecuto..."

loop = asyncio.get_event_loop()

try:
    asyncio.ensure_future(main())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()


#for us in lista2:
#if us[4]==datos[4]:
#new_users.remove(i)
#if u.username is None :
# u.username = []
# fullstring = u.username
#if substring in fullstring:
# print ("Found! ")
# else:
#print ("Not found!" + u.username)
#with TelegramClient("new", api_id, api_hash) as client:  
#bot.send_message(1204307512, 'mensaje de prueba')
#bot.send_message(1204307512, 'Use inline keyboard')
#Enviar()
#@client.on(events.UserUpdate)
