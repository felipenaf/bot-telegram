import os
import telebot

bot = telebot.TeleBot(os.environ['BOT_API_TOKEN'])
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, u"Olá, bem-vindo ao bot!")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, u"Esse bot foi desenvolvido por Felipe Ferreira!")

#inicializa o bot
bot.polling()
