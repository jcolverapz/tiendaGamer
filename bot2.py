from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import ChannelParticipantsKicked 
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.types import InputChannel
from telethon.tl.types import InputPeerEmpty
from telegram.ext.filters import Filters
from telethon.tl.functions.channels import JoinChannelRequest
import asyncio

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
################################################
channel_username = '@pruebastienda'
# Create the client and connect
client = TelegramClient('sessionname', api_id, api_hash)  # feel free to edit %sessionname% as you want
client.connect()
client.start()

entity = client.get_entity("t.me/pruebastienda") #omit @
#Luego, invoque esta función.
print(entity)
client(JoinChannelRequest(entity))

def new_user(update, context):
    update.message.reply_text("New user joined")
    #print('New User Joined')

from telethon.sync import TelegramClient
from telethon import functions, types

with TelegramClient("session", api_id, api_hash) as client:
    result = client(functions.contacts.BlockRequest(
        id=1204307512
    ))
    print(result)
#Members:
#user_added (bool):
#client.run_until_disconnected()

     keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Press me', callback_data='press')],
        ])
    
    
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
            # print("Enviado"
            bot.send_message(1511413607, 'mensaje de prueba')
        except:
            print("")
        
        print('mensaje enviado a ' + str(i[0]))
    """
        # main()
        #lista1 = lista2
       # print('lista1:' + str(lista1))
        print('finalizo el evento')

# content of the automatic reply
#message= "@dante_dog_bot"

if __name__ == '__main__':
    # Create the client and connect
    # use sequential_updates=True to respond to messages one at a time
    #client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)

    @client.on(events.NewMessage(pattern='(?i)mala atención.+'))
    async def handler(event):
        # Respond whenever someone says "Hello" and something else
        await event.reply('Te pido disculpas!')

    @client.on(events.NewMessage(outgoing=True, pattern='nada'))
    async def handler(event):
        # Say "!pong" whenever you send "!ping", then delete both messages
        m = await event.respond('!Ok')
        await asyncio.sleep(5)
        await client.delete_messages(event.chat_id, [event.id, m.id])


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