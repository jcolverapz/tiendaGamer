def request_phone(cls, text, *,
                      resize=None, single_use=None, selective=None):
        """
        Creates a new keyboard button to request the user's phone on click.
        ``resize``, ``single_use`` and ``selective`` are documented in `text`.
        When the user clicks this button, a confirmation box will be shown
        to the user asking whether they want to share their phone with the
        bot, and if confirmed a message with contact media will be sent.
        """
        return cls(types.KeyboardButtonRequestPhone(text),
                   resize=resize, single_use=single_use, selective=selective)

TOKEN = '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0'
#bot = telebot.TeleBot(TOKEN)

# Initialize bot
bot <- Bot(token = "TOKEN")
chat_id <- "CHAT_ID"

# Create Inline Keyboard
text <- "Could you type their phone number, please?"
IKM <- InlineKeyboardMarkup(
  inline_keyboard = list(
    list(
      InlineKeyboardButton(1),
      InlineKeyboardButton(2),
      InlineKeyboardButton(3)
    ),
    list(
      InlineKeyboardButton(4),
      InlineKeyboardButton(5),
      InlineKeyboardButton(6)
    ),
    list(
      InlineKeyboardButton(7),
      InlineKeyboardButton(8),
      InlineKeyboardButton(9)
    ),
    list(
      InlineKeyboardButton("*"),
      InlineKeyboardButton(0),
      InlineKeyboardButton("#")
    )
  )
)