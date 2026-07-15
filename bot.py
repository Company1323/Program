import telebot
import os

# خواندن توکن از تنظیمات سرور (به جای نوشتن مستقیم)
TOKEN = os.environ.get('8626556930:AAEmjnj2YqBrsdku6uEJQjbrr7mMUBBUsk0')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ربات فعال شد!")

bot.infinity_polling()