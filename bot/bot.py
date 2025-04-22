from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

# Запуск простого HTTP-сервера для Render (порт 8080)
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'whylovly bot is running')

def run_http_server():
    server = HTTPServer(('0.0.0.0', 8080), SimpleHandler)
    server.serve_forever()

# Запуск сервера в отдельном потоке
threading.Thread(target=run_http_server, daemon=True).start()

# Telegram-бот
TOKEN = os.getenv("API_TOKEN")  # токен из Render → Environment
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Привет! Это whylovly\n\n"
        "Нажав на кнопку Blog ты перейдешь на мой профиль, "
        "в нем ты найдешь фото, видео, музыку и скрытый архив с заданиями.\n"
    )

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.answer(
        "Вот подсказки к заданиям:\n\n"
        "2. Слово написано на футболке на первом посте, вписывай его с большой буквы на английском.\n"
        "3. Первое слово:\n"
        "Без крика кричат, без слов говорят,\n"
        "На щеках оставляют солёный след.\n"
        "Не кровь, не вода — но падают вниз.\n\n"
        "Второе слово:\n"
        "Он без цвета, без огня,\n"
        "Касается — и нет тепла.\n"
        "Заставит кожу задрожать,\n"
        "Зимой он любит навещать.\n\n"
        "Третье слово:\n"
        "Реально - ***** . мне безразлично.\n\n"
        "Вписывай все слова с большой буквы без пробела — например: НапримерТестПароль\n\n"
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
