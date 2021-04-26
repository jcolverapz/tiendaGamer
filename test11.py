import sys
import telepot 
import time
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardHide, ForceReply


#Token = "XXXYYY:XXYY"
TOKEN = '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0'

bot = TelegramClient("bot", YYYY, "XXXX").start(bot_token=Token)


@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    """Send a message when the command /start is issued."""
    await event.respond('Hi!')
    raise events.StopPropagation


@bot.on(events.NewMessage)
async def echo(event):
    """Echo the user message."""
    print(f">> get it {event.text}")
    await event.respond(event.text)


def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()