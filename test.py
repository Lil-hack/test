import telebot
bot = telebot.TeleBot('1083122436:AAGRyeJSDNNN6i92-Xz1GIOv9huSdqvIVPM')

@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.send_message(message.chat.id, 'sdf')

print('lox')
bot.polling(none_stop=True, interval=0)