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
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#import utils
#from telethon.tl.types import ChannelAdminLogEventAction
import asyncio
from datetime import datetime

"""
api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@micanaljc'  
#i=0
################################################
now = datetime.now()
#      Create the client and connect
client = TelegramClient('newsession', api_id, api_hash)  # feel free to edit %sessionname% as you want
client.connect() # logining and connecting to Telegram servers
client.start()
"""
#import numpy as np
import gspread
#from oauth2client.service_account import ServiceAccountCredentials
#scope = ["https://spreadsheets.google.com/feeds​",'https://www.googleapis.com/auth/sprea...​,"https://www.googleapis.com/auth/drive...​","https://www.googleapis.com/auth/drive​"]
#creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
#client=gspread.authorize(creds)
#open_by_key()
#sheet=client.open("tutorial").sheet1
#sheet.update_acell('B1','Bingo')
gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key("1rarTmHh1dbD6oIpLIeHQiBhZ5EV2QyurniUSdi4nA_w") # or by sheet name: gc.open("TestList")
worksheet = sh.worksheet("suscriptores") 

def test():
    print("funciona")
    res=[]
    res = sh.worksheet("contactos").get_all_records() # list of dictionaries
    #print(res)
    #print(len(res))
    #items = res.items()
    #my_array = np.array(res)
    #print(my_array)
    
       

def agregar(arg): 
    #worksheet.append_row(1)
    #worksheet.insert_row(user,3)
    ### retrieve data ###
    #texto= texto.raw_text.split(",")
    worksheet.append_row(arg)


def buscar():
    lista1=[]
    lista1.clear()
    #res= worksheet.get('B2')
    #res = worksheet.get_all_records() # list of dictionaries
    #res = worksheet.get_all_records(head=0))
    #res = worksheet.get_all_values()) # list of lists
    res= worksheet.col_values(1)
    for i in res:
        try:
            #print(type(int(i)))
            lista1.append(int(i))
        except:
            
            print("An exception occurred")

    return lista1

def actualizar(rw, arg):
    print('actualizar')
    #res= worksheet.range('A2:A20')
    #for i in res:
        #print(i)
    
       # if int(rw) == int(i):
   # worksheet.update_cell(rw, 6, arg)
    #worksheet.update_cell(rw, 7, arg)
    #print(rw)
    cell = worksheet.find(str(rw), in_column=1)
    worksheet.update_cell(cell.row, 7, arg)
    #worksheet.update_cell(cell.row, 9, 'test')
    #print('celda actualizada'  + str(cell.row))

# print(cell)
# print("Found something at R%sC%s" % (cell.row, cell.col))

def tipo(arg):
    #print('tipiando')
    #res= worksheet.get('B2')
    #contacto = sh.worksheet("Contactos").cell(2,2).value
    
    try:
        cell = worksheet.find(str(arg),in_column=1)
       #print(cell.row)
    #valor1 = worksheet.cell(cell.row, 6).value

    #agendo = worksheet.cell(cell.row, 6).value
        if worksheet.cell(cell.row, 7).value=="SI":
            tipo=1
    #Compro=No, Agendo=No
        elif worksheet.cell(cell.row, 6).value=="SI" and worksheet.cell(cell.row, 7).value=="NO":
            tipo=2
        else:
        #worksheet.cell(cell.row, 6).value=="NO" and worksheet.cell(cell.row, 7).value=="NO"
            tipo=3
    except:
        #print("Exception")
        tipo=4
    #if agendo==False:
    #msj = sh.worksheet("mensajes").cell(2,2).value
    #print(agendo)
    #print('mensaje' + str(tipo))
    return (int(tipo))

def datos():
    #contactos=[]
    #contactos.clear()
    #res= worksheet.get('B2')
    #res = worksheet.get_all_records() # list of dictionaries
    res = sh.worksheet("contactos").get_all_records()
    #res = worksheet.get_all_values()) # list of lists
    #res= worksheet.col_values(1)
    return res


def main():
    test()


if __name__ == '__main__':
    main()
 
'''
for i in res:
        try:
            #print(type(int(i)))
            lista1.append(int(i))
        except:
            print("An exception occurred")
    return lista1

#Contamos con Servicio técnico PROPIO , para resolver cualquier duda o inconveniente que tengas a la brevedad.
#Contamos con más de 1 año de experiencia en el rubro y trabajamos con más de 1500 revendedores.


@client.on(events.NewMessage(pattern=r'(?i).*\b(Cotizacion|hi)\b'))
async def handler(event):

    # Respond whenever someone says "Hello" and something else
    #await event.respond(mensaje)
    #await client.send_message('@zeidardz', 'Welcome')
   
#@register(outgoing=True, pattern="^\.button(?: |$)(.*)")
#async def buttontest(test):
    #await test.client.send_message(test.chat_id, 'click me', buttons=[Button.inline('Test', 'test-return')])

 

await event.reply('Hey!')
sender = await event.get_sender()
name = utils.get_display_name(sender)
await event.reply('hi!')
'''
