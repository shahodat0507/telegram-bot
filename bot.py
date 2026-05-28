import telebot

TOKEN = "TOKENINGIZNI_BU_YERGA_YOZING"
bot = telebot.TeleBot(TOKEN)

admin_id = 8425724360


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "Assalomu alaykum! Murojaatingizni yuboring."
    )


@bot.message_handler(func=lambda message: True)
def handle_message(message):

    # Admin javobi
    if message.chat.id == admin_id and message.reply_to_message:

        try:
            user_id = message.reply_to_message.forward_from.id

            bot.send_message(user_id, message.text)

            bot.reply_to(message, "✅ Javob yuborildi")

        except:
            bot.reply_to(message, "❌ Javob yuborilmadi")

        return

    # User xabarini adminga yuborish
    bot.forward_message(
        admin_id,
        message.chat.id,
        message.message_id
    )


print("Bot ishga tushdi...")
bot.infinity_polling()
