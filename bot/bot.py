from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

TOKEN = os.getenv("API_TOKEN")  # токен из настроек Render

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Привет! Это whylovly\n\n"
        "Нажав на кнопку Blog ты перейдешь на мой профиль, в нем ты найдешь фото, видео, музыку и скрытый архив с заданиями.\n"
        "Если будут проблемы с заданиями, напиши /help сюда в чат, чтобы получить подсказки по заданиям."
    )

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.answer(
        "Вот подсказки к заданиям:\n\n"
        "2. Слово написано на футболке на первом посте, вписывай его с большой буквы на английском. \n"
        "3. Первое слово\n"
        "Без крика кричат, без слов говорят,\n"
        "На щеках оставляют солёный след.\n"
        "Не кровь, не вода — но падают вниз.\n\n"
        "Второе слово\n"
        "Он без цвета, без огня,\n"
        "Касается — и нет тепла.\n"
        "Заставит кожу задрожать,\n"
        "Зимой он любит навещать.\n\n"
        "Третье слово\n"
        "Реально - ***** . мне безразлично."
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
