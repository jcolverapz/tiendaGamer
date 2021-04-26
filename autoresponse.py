import time

from telethon import TelegramClient, events

# sample API_ID from https://github.com/telegramdesktop/tdesktop/blob/f98fdeab3fb2ba6f55daf8481595f879729d1b84/Telegram/SourceFiles/config.h#L220
# or use your own

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
# fill in your own details here
phone = '+528132341246'

session_file = '/path/to/session/file'  # use your username if unsure
#password = 'YOUR_PASSWORD'  # if you have two-step verification enabled

# content of the automatic reply
message = "Sorry, I'll be away until next week!"

if __name__ == '__main__':
    # Create the client and connect
    # use sequential_updates=True to respond to messages one at a time
    #client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)

    client = TelegramClient('newsession', api_id, api_hash)
    
    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        if event.is_private:  # only auto-reply to private chats
            from_ = await event.client.get_entity(event.from_id)  # this lookup will be cached by telethon
            if not from_.bot:  # don't auto-reply to bots
                print(time.asctime(), '-', event.message)  # optionally log time and message
                time.sleep(1)  # pause for 1 second to rate-limit automatic replies
                await event.respond(message)


    print(time.asctime(), '-', 'Auto-replying...')
    #client.connect() # logining and connecting to Telegram servers
    client.start()
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')