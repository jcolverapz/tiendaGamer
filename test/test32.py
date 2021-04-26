
#async def main():
    #async with TelegramClient('sessionname', api_id, api_hash)  as client:
    #     notice these parenthesis
    #     You want to 'await' the call, not the username
    # message = await client.send_message('me', 'Hi!')
    #await asyncio.sleep(5)
    #await message.delete()

@client.on(events.NewMessage(pattern='(?i)hi|hello'))
async def handler(event):
    await event.reply('hey')
    await client.run_until_disconnected()

loop = asyncio.get_event_loop()

# Register the update handler so that it gets called


#async def main():
    #bot = TelegramClient(NAME, API_ID, API_HASH)
    #await bot.start(bot_token=TOKEN)
#if not client.is_user_authorized():  # authorization (if there is no .session file created before)
   # client.send_code_request(phone_number)
   # client.sign_in(phone_number, input('Enter the code: '))
   
# this was as a test to see how do I fetch stuff
#result = client(ResolveUsernameRequest('pruebastienda'))
#found_chats = result.chats
#found_users = result.users

#r = client(GetFullChannelRequest(result.chats[0]))

#x = client(GetParticipantsRequest(found_users[0]))
#result = client(ResolveUsernameRequest('username'))
# end test
#def GetFullChannel(self, id):
   # self.GetFullChatRequest(id)

#users = client(GetFullChannel(self, 'id'))
#response = client.invoke(GetFullChatRequest(id))
#r = client(GetFullChatRequest(id))

#loop.run_until_complete(main())