import telebot
import random

token = "1672342091:AAFA4--XfPc9tKwr3Oo9CVe2LVtdf9Q8Yt4"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, "به ربات خودتون خوش آمدید.")
    bot.send_message(message.chat.id, "اگر میخوای نشون بدی چقدر باهوشی یک عدد از 1 تا 20 بگو ببینم:")


com = random.randint(1, 20)


@bot.message_handler(func=lambda message: True)
def normal_message(message):
    user = int(message.text)
    if user < com:
        bot.reply_to(message, "عدد بزرگتر قرار بده عزیزم")

    elif user > com:
        bot.reply_to(message, "عدد کوچکتر قرار بده عزیزم")

    elif user == com:
        audio = open("sound.ogg", "rb")
        bot.send_audio(message.chat.id, audio)
        bot.send_message(message.chat.id, "/start  آیا دوست داری دوباره بازی کن")

    else:
        bot.reply_to(message, "What")


bot.polling()
