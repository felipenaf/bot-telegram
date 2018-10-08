import os
import telebot
import time

def find_at(msg):
    for text in msg:
        if '@' in text:
            return text

bot = telebot.TeleBot(os.environ['BOT_API_TOKEN'])
@bot.message_handler(commands=['start'])
def bem_vindo(message):
    bot.reply_to(message, u"Olá, seja bem-vindo ao bot!")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, u"Esse bot foi desenvolvido por Felipe Ferreira!")

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_answer(message):
    texts = message.text.split()
    at_text = find_at(texts)
    bot.reply_to(message, 'https://instagram.com/{}'.format(at_text[1:]))

while True:
    try:
        #inicializa o bot
        bot.polling()
    except Exception:
        time.sleep(15)


