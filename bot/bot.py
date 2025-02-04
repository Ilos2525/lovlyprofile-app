import telebot

# Твой токен
TOKEN = "7854822671:AAEeCkjZ4gOs4KkCf4g-rk8UsnIo_BNHGMw"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    web_app_button = telebot.types.InlineKeyboardButton(
        text="Открыть приложение",
        web_app=telebot.types.WebAppInfo("https://Ilos2525.github.io/lovlyprofile-app/")
    )
    keyboard.add(web_app_button)
    
    bot.send_message(message.chat.id, "Привет! Нажми кнопку, чтобы открыть Web App:", reply_markup=keyboard)

print("Бот запущен!")
bot.polling(none_stop=True)
