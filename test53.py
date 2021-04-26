with bot.conversation(chat) as conv:
    conv.send_message('Hi!')
    hello = conv.get_response()

    conv.send_message('Please tell me your name')
    name = conv.get_response().raw_text
    while not any(x.isalpha() for x in name):
        conv.send_message("Your name didn't have any letters! Try again")
        name = conv.get_response().raw_text

    conv.send_message('Thanks {}!'.format(name))