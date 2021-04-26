from telethon import TelegramClient, Button, events

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@micanaljc'

#bot = TelegramClient(...)
bot = TelegramClient('newsession', api_id, api_hash)  # feel free to edit %sessionname% as you want
#client.connect() # logining and connecting to Telegram servers
bot.start()

async def main():
    async with bot:
        # Needed to find the username of the bot itself,
        # to link users to a private conversation with it.
        me = await bot.get_me()

        @bot.on(events.ChatAction)
        async def handler(event):
            if event.user_joined:
                # Don't let them send messages
                await bot.edit_permissions(event.chat_id, event.user_id, send_messages=False)

                # Send a message with URL button to start your bot with parameter "captcha"
                url = f'https://t.me/{me.username}?start=captcha'
                await event.reply(
                    'Welcome! Please solve a captcha before talking',
                    buttons=Button.url('Solve captcha', url))

        # Detect when people start your bot with parameter "captcha"
        @bot.on(events.NewMessage(pattern='/start captcha'))
        async def handler(event):
            # Make them solve whatever proof you want here
            await event.respond('Please solve this captcha: `1+2 = ?`')
            # ...more logic here to handle the rest or with more handlers...
    
        await bot.run_until_disconnected()