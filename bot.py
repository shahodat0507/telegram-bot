import telebot
from flask import Flask
from threading import Thread
import os

TOKEN = "8784214206:AAGVgFPVVGabD4A9Yl-RHHYKxlxWMIxcET0"

bot = telebot.TeleBot(TOKEN)

admin_id = 8425724360


app = Flask('')

@app.route('/')
def home():
    return "Bot ishlayapti!"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))

Thread(target=run).start()


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "Assalomu alaykum! Xabaringizni yuboring."
    )


@bot.message_handler(func=lambda message: True)
def handle_message(message):

    # Admin reply qilsa
    if (
        message.chat.id == admin_id
        and message.reply_to_message
        and message.reply_to_message.forward_from
    ):

        try:
            user_id = message.reply_to_message.forward_from.id

            bot.send_message(user_id, message.text)

            bot.reply_to(message, "✅ Javob yuborildi!")

        except:
            bot.reply_to(
                message,
                "❌ Bu xabarga javob yuborib bo‘lmadi."
            )

        return

    # User xabarini adminga forward qilish
    bot.forward_message(
        admin_id,
        message.chat.id,
        message.message_id
    )

    info = f"""
👤 Ism: {message.from_user.first_name}
🆔 ID: {message.from_user.id}
"""

    bot.send_message(admin_id, info)


print("Bot ishga tushdi...")
bot.infinity_polling()
