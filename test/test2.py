from telethon import TelegramClient

api_id=3409046
api_hash='48ae9fbdf79edda291e1fa5796fc4665'
bot = TelegramClient('miname', api_id, api_hash)
#bot.start(bot_token='1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0')
bot.start()
async def main():
#Now you can use all client methods listed below, like for example...
    await bot.send_message('me', 'Hello to myself!')
updater= Updater('1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0')
updater.start_polling()

list = [0,100,200,300]


def __init__(self, client, chat, action, *, delay, auto_cancel):
        self._client = client
        self._chat = chat
        self._action = action
        self._delay = delay
        self._auto_cancel = auto_cancel
        self._request = None
        self._task = None
        self._running = False
  # Only used for channels, but we should always set the attribute
        self.requests = []
        self.total = ( self.client(
           functions.channels.GetFullChannelRequest('pruebastienda')
           )).full_chat.participants_count
print (self.total)

if last_message != new_message:
      with client:
          client.loop.run_until_complete(send_mess(message=new_message))
          last_message = new_message

          
@client.on(events)



@client.on(events.ChatAction)
async def handler(event):
    # Welcome every new user
    if event.user_joined:
        await event.reply('Welcome to the group!')
def main():
    

    @client.on(events.NewMessage(chats=[PeerChannel(123456789)]))
async def my_event_handler(event):
    print(event.raw_text)
Or:

@client.on(events.NewMessage(chats=[-100123456789]))
async def my_event_handler(event):
    print(event.raw_text)

    from telethon.tl.functions.channels import JoinChannelRequest
 
await client(JoinChannelRequest(channel_username))
print("Client Created")
entity = client.get_entity("t.me/pruebastienda") #omit @
#Luego, invoque esta función.
client(JoinChannelRequest(entity))

# In the same way, you can also leave such channel
from telethon.tl.functions.channels import LeaveChannelRequest
client(LeaveChannelRequest(input_channel))

from telethon.tl.functions.messages import AddChatUserRequest

client(AddChatUserRequest(
    chat_id,
    user_to_add,
    fwd_limit=10  # allow the user to see the 10 last messages
))

from telethon.tl.functions.channels import JoinChannelRequest
channels.joinChannel#24b524c5 channel:InputChannel = Updates


# get all the channels that I can access
channels = {d.entity.username: d.entity
            for d in client.get_dialogs()
            if d.is_channel}


 
async def main():
    