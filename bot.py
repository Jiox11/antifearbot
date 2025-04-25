
import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# Start command
@bot.message_handler(commands=["start"])
def start_handler(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("💳 Get Your Motivation Guide", callback_data="buy_pdf"))
    bot.send_message(
        message.chat.id,
        "👋 Welcome, brave soul!\n\n"
        "Are you tired of fear controlling your destiny? Do you dream of becoming stronger, sharper, and unstoppable?\n\n"
        "We have created something special — the *Anti-Fear Motivation Guide* — a powerful PDF manual crafted to help you crush doubts, build discipline, and unlock your true potential.\n\n"
        "Click the button below and take the first step toward your transformation. The journey of strength and confidence starts now!",
        parse_mode="Markdown",
        reply_markup=markup
    )

# Button callback
@bot.callback_query_handler(func=lambda call: call.data == "buy_pdf")
def buy_pdf_handler(call):
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "💳 To receive your *Anti-Fear Motivation Guide*, please send $5 to the card number below:\n\n"
        "`4400 6649 5765 3521`\n\n"
        "After completing the payment, simply type 'paid' here, and your guide will be delivered automatically!",
        parse_mode="Markdown"
    )

# Handle 'paid' message
@bot.message_handler(func=lambda message: message.text.lower() == "paid")
def send_pdf(message):
    try:
        with open("AntiFear_Motivation_Guide.pdf", "rb") as pdf:
            bot.send_document(message.chat.id, pdf)
            bot.send_message(
                message.chat.id,
                "✅ Thank you for your trust! Here is your guide.\n\nStay fearless. Stay disciplined. Your journey has just begun. 🚀"
            )
    except FileNotFoundError:
        bot.send_message(message.chat.id, "❌ Sorry, the file was not found. Please contact support.")

bot.polling()
