import telebot

TOKEN = "8361921715:AAElpzMWptf-htcIswfWIdMs5c1JeOtvRWw"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom! 👋\nMenga nima yozsang, shuni qaytaraman.")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.send_message(message.chat.id, message.text)

bot.infinity_polling()
