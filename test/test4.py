from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import GetFullChannelRequest

api_id=3409046
api_hash='48ae9fbdf79edda291e1fa5796fc4665'
channel = '@pruebastienda'
# Create the client and connect
client = TelegramClient('sessionname', api_id, api_hash)  # feel free to edit %sessionname% as you want
client.connect()

# code using client...

with client:
        #client.loop.run_until_complete(main())
    async def join(client):
   # ch = '@andeh_ir'
        try:
            await client(JoinChannelRequest(channel))
            print('[+] Joined The Channel')
        except:
            print('[-] skiped')
    #with TelegramClient('sessionname', api_id, api_hash) as client:
    #   result = client(functions.channels.JoinChannelRequest(
    #      channel='@pruebastienda'
    # ))
    #print(result.stringify())


misusuarios =  client.get_participants('@pruebastienda')
while True:
    try:
        update = client.updates.poll()
        if not update:

            continue

        print('I received', update)
    except KeyboardInterrupt:
        break