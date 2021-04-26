import sys
import telepot
from telepot.delegate import per_chat_id, create_open

class MessageCounter(telepot.helper.ChatHandler):
    def __init__(self, seed_tuple, timeout):
        super(MessageCounter, self).__init__(seed_tuple, timeout)
        self._count = 0

    def on_message(self, msg):
        self._count += 1
        self.sender.sendMessage(self._count)
TOKEN = '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0'
#bot = telebot.TeleBot(TOKEN)
#TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.DelegatorBot(TOKEN, [
    (per_chat_id(), create_open(MessageCounter, timeout=10)),
])

#bot.notifyOnMessage(run_forever=True)