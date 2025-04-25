
import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# Helper function to log users
def log_user(user_id, first_name, username, action):
    with open("users.txt", "a", encoding="utf-8") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"Time: {now} | User ID: {user_id} | Name: {first_name} | Username: @{username} | Action: {action}\n")

# Start command
@bot.message_handler(commands=["start"])
def start_handler(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("💳 Get Your Motivation Guide", callback_data="buy_pdf"))
    
    # Log user when they press /start
    log_user(
        user_id=message.from_user.id,
        first_name=message.from_user.first_name,
        username=message.from_user.username if message.from_user.username else "no_username",
        action="/start"
    )

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
        "After completing the payment, simply type 'paid' here, and wait for manual verification.",
        parse_mode="Markdown"
    )

# Handle 'paid' message manually
@bot.message_handler(func=lambda message: message.text.lower() == "paid")
def manual_verification(message):
    # Log user when they write "paid"
    log_user(
        user_id=message.from_user.id,
        first_name=message.from_user.first_name,
        username=message.from_user.username if message.from_user.username else "no_username",
        action="paid"
    )

    bot.send_message(
        message.chat.id,
        "✅ Thank you! Your payment will be verified manually.\n\n"
        "Please wait while our team checks your payment. We will send you the guide shortly!"
    )

bot.polling()
