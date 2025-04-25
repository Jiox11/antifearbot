
import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# Start message with Buy button
@bot.message_handler(commands=["start"])
def start_handler(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("💳 Buy PDF Guide", callback_data="buy_pdf"))
    bot.send_message(
        message.chat.id,
        "👋 Welcome, warrior! Ready to overcome fear and unlock your discipline?\n\n"
        "Click the button below to get access to our exclusive Anti-Fear Motivation Guide:",
        reply_markup=markup
    )

# Button press: show payment instructions
@bot.callback_query_handler(func=lambda call: call.data == "buy_pdf")
def buy_pdf_handler(call):
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "💳 To receive your PDF guide, please send a payment of $5 to this card number:

"
        "`4400664957653521

"
        "After sending, reply here with a screenshot or write: 'paid'."
    )

# Manual keyword "paid" triggers PDF send (you verify and confirm manually)
@bot.message_handler(func=lambda message: message.text.lower() == "paid")
def send_pdf(message):
    with open("AntiFear_Motivation_Guide.pdf", "rb") as pdf:
        bot.send_document(message.chat.id, pdf)
        bot.send_message(message.chat.id, "✅ Here is your guide. Stay strong and consistent!")

bot.polling()
