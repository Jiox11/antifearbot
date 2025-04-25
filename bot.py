
import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start_handler(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("💳 Get PDF Guide", callback_data="buy_pdf"))
    bot.send_message(
        message.chat.id,
        "👋 Privet, warrior! You want to crush fear and build discipline?

"
        "Click da button below to unlock your personal Motivation Guide in PDF format.",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == "buy_pdf")
def buy_pdf_handler(call):
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "💳 Send 5$ to the card below:

"
        "`4400 6649 5765 3521`

"
        "After that — just reply 'paid' or drop screenshot here.",
        parse_mode="Markdown"
    )

@bot.message_handler(func=lambda message: message.text.lower() == "paid")
def send_pdf(message):
    try:
        with open("AntiFear_Motivation_Guide.pdf", "rb") as pdf:
            bot.send_document(message.chat.id, pdf)
            bot.send_message(message.chat.id, "✅ Guide delivered. Stay focused, stay sharp.")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "❌ File not found. Please contact support.")

bot.polling()
