import telebot
import time

bot = telebot.TeleBot("698575115:AAHcK4l_xN6dwaYVXNtHiE66hXAldYibtAQ")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Olá, seja bem vindo")

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "Esse é um bot de teste feito pelo Bipão")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "Tudo bem ?":
	    bot.reply_to(message, "Td sim " + message.from_user.first_name + ", e vc?")

while True:
    try:
        #inicializa o bot
        bot.polling()
    except Exception:
        time.sleep(15)