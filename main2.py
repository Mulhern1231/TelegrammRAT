import telebot
import os
import requests


class error:
    NoneName = 'Вы не состоите в группе админов'

token = "5056136508:AAGkP-SCb3fe_9yaG3qq0wC1BxqAmSM4I8w"
bot = telebot.TeleBot(token)


ip = requests.get('https://checkip.amazonaws.com').text.strip()


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.from_user.id, """
					Доступные команды:
					 - /off - выключить ПК
					 - /status - Статус ПК
					 - /ip - Вывести все ip в сети
					""")

@bot.message_handler(content_types=['text'], commands=["ip"])
def ip(message):
    if str(message.from_user.id) == "42615643":
        bot.send_message(message.from_user.id, ip)
    else:
        bot.send_message(message.from_user.id, error.NoneName)

@bot.message_handler(content_types=['text'], commands=["off"])
def off(message):
    bot.send_message(message.from_user.id, "отправьте IP")
    bot.register_next_step_handler(message, get_ip)

def get_ip(message):
    global ip_select
    ip_select = message.text

    if str(ip) == ip_select:
        bot.send_message(message.from_user.id, f'Компьютер ({ip}) выключен')
        os.system('shutdown -p')


bot.polling(none_stop=True, interval=0)
