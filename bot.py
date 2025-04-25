
import os
import telebot

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, (
        "👋 Welcome, warrior.\n\n"
        "You didn’t come here by accident. You showed up because something inside you refuses to settle.\n\n"
        "This bot is more than text — it's a space for discipline, courage, and mental growth.\n"
        "Every step you take here is a step toward the strongest version of yourself.\n\n"
        "🔥 Inside, you'll find motivational digital guides, tools to overcome fear, and powerful reminders to stay committed.\n"
        "Discipline is not about feeling ready — it's about showing up, even when you’re not.\n"
        "Courage is not about being fearless — it’s about moving forward in spite of fear.\n\n"
        "Want your first motivational PDF guide?\n"
        "Just type: paid\n"
        "Let’s turn your drive into direction. Let’s go."
    ))

@bot.message_handler(func=lambda message: message.text.lower() == "paid")
def send_pdf(message):
    with open("AntiFear_Motivation_Guide.pdf", "rb") as pdf:
        bot.send_document(message.chat.id, pdf)
        bot.send_message(message.chat.id, 
            "✅ Here’s your guide.\n"
            "Take your time. Absorb it. Apply it.\n"
            "And remember — the discipline to keep going is your ultimate power. Keep rising."
        )

bot.polling()
