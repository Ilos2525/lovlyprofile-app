from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Твой токен
TOKEN = "7854822671:AAEeCkjZ4gOs4KkCf4g-rk8UsnIo_BNHGMw"

bot = Bot(token=API_TOKEN)
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
        "3. Первое слово 
Без крика кричат, без слов говорят,
На щеках оставляют солёный след.
Не кровь, не вода — но падают вниз.

Второе слово 
Он без цвета, без огня,
Касается — и нет тепла.
Заставит кожу задрожать,
Зимой он любит навещать.

Третье слово 
Реально - ***** . мне безразлично."
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

