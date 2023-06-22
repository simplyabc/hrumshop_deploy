import telebot

bot = telebot.TeleBot('6017243361:AAH3uV6luTA9c0EnlFHTqmiwSIcGF4_Whks')

chat_id = 758700579


def send_message(message):
    cart_data = '\n'.join(message['cart_data'][i]['name'] + '   ' +
                          message['cart_data'][i]['weight'] + ' гр.   ' +
                          message['cart_data'][i]['price'] + ' ₽   ' +
                          message['cart_data'][i]['quantity'] + ' шт.'
                          for i in message['cart_data'].keys())

    bot.send_message(chat_id,
                     f"""
Заказ № {message['id']}

Имя: {message['name']}
Телефон: {message['phone']}
Адрес: {message['address']}

Комментарий: {message['comments']}

Состав доставки:

{cart_data}

Сумма: {message['cart_total_price']} ₽
""")


