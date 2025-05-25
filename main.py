import telebot
from telebot import types
from datetime import datetime

# ✅ Token ou deja mete
BOT_TOKEN = "7738109275:AAE8twsA59WqpizEnYjN_LVToFLH6sWLrhQ"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🟢 Trade UP")
    btn2 = types.KeyboardButton("🔴 Trade DOWN")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "👋 Byenvini! Chwazi yon aksyon:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_trade(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if message.text == "🟢 Trade UP":
        bot.reply_to(message, f"🟢 Ou chwazi UP a {now}")
    elif message.text == "🔴 Trade DOWN":
        bot.reply_to(message, f"🔴 Ou chwazi DOWN a {now}")
    else:
        bot.reply_to(message, "❓ Tanpri chwazi youn nan bouton yo.")

bot.infinity_polling()
