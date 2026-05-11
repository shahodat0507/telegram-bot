from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot ishlayapti!"

def run_web():
    app.run(host="0.0.0.0", port=10000)

threading.Thread(target=run_web).start()

import telebot

TOKEN= "8784214206:AAFYgqbF9GNfQFWgyxE6Rzu21VAlRLtV7FQ"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Assalomu alaykum! Murojaatingizni yuboring.")

@bot.message_handler(func=lambda message: True)
def forward_message(message):
    if message.chat.id == admin_id and message.reply_to_message:
        text = message.reply_to_message.text
        user_id = int(text.split("ID ")[1].split("\n")[0])

        bot.send_message(user_id, message.text)
        return
    admin_id = 8425724360
    
    text = f"""
📩 Yangi murojaat

👤 {message.from_user.first_name}
🆔 {message.from_user.id}
✉️ {message.text}
"""

    bot.send_message(admin_id, text)

print("Bot ishga tushdi...")
bot.infinity_polling()

