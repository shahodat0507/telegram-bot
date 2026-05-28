import telebot
TOKEN = "8784214206:AAH7yyhmHgnZtGfWzuGh_TX88X1IZLP7Gis"
bot = telebot.TeleBot(TOKEN)

admin_id = 8425724360

reply_map = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Assalomu alaykum! Murojaatingizni yuboring.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):

    if message.chat.id == admin_id and message.reply_to_message:
        reply_msg_id = message.reply_to_message.message_id
        user_id = reply_map.get(reply_msg_id)

        if user_id:
            bot.send_message(user_id, message.text)
            bot.send_message(admin_id, "✅ Javob yuborildi.")
        else:
            bot.send_message(admin_id, "❌ Bu xabarga javob yuborib bo‘lmadi. Yangi kelgan murojaatga Reply qiling.")
        return

    text = f"""📩 Yangi murojaat

👤 Ism: {message.from_user.first_name}
ID: {message.from_user.id}

✉️ Xabar: {message.text}
"""

    sent = bot.send_message(admin_id, text)
    reply_map[sent.message_id] = message.from_user.id

print("Bot ishga tushdi...")
bot.infinity_polling()
