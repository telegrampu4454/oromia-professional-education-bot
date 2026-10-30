
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "YOUR_BOT_TOKEN"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton("📚 Subjects"),
        KeyboardButton("📖 Notes")
    )
    keyboard.add(
        KeyboardButton("📝 MCQs"),
        KeyboardButton("🎯 Exams")
    )
    keyboard.add(
        KeyboardButton("🌍 Language"),
        KeyboardButton("ℹ️ About")
    )

    bot.send_message(
        message.chat.id,
        "Welcome to OROMIA PROFESSIONAL EDUCATION BOT! 🎓\n\nChoose what you want to learn:",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: True)
def menu(message):
    if message.text == "📚 Subjects":
        bot.reply_to(message, "Available subjects:\nBiology\nChemistry\nPhysics\nMathematics\nEnglish")
    elif message.text == "📖 Notes":
        bot.reply_to(message, "Study notes will be available here soon.")
    elif message.text == "📝 MCQs":
        bot.reply_to(message, "Practice MCQs will be available here soon.")
    elif message.text == "🎯 Exams":
        bot.reply_to(message, "Practice exams will be available here soon.")
    elif message.text == "🌍 Language":
        bot.reply_to(message, "Languages: English and Afaan Oromoo.")
    elif message.text == "ℹ️ About":
        bot.reply_to(message, "Your educational learning partner! 🎓")
    else:
        bot.reply_to(message, "Please choose an option from the menu.")

bot.infinity_polling()
