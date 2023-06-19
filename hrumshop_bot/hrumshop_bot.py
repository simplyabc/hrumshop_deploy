from telebot import TeleBot
from hrumshop.cart.views import OrderAdd
bot = TeleBot('6017243361:AAH3uV6luTA9c0EnlFHTqmiwSIcGF4_Whks')


@bot.message_handler(commands=['start'])
def get_text_message(message):
    while True:
        bot.send_message(message.chat.id, str(input()))


bot.infinity_polling()
