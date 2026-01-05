import os
import telebot

# TOKEN Render'dan olinadi (Environment Variable)
TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Salom 👋\n"
        "Bu mening birinchi Telegram botim.\n\n"
        "Menga nima yozsang, shuni qaytaraman 😊"
    )

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, message.text)

# Botni doimiy ishlatish
bot.infinity_polling()

