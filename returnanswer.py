import telebot

bot = telebot.TeleBot('6079281262:AAEIHZp5-xWQ57ledodWLRcjOgdhxwF7TWw')


@bot.message_handler()
def echo_message(message):
    bot.reply_to(message, message.text)


bot.polling()
