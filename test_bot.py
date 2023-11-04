from aiogram import Bot, Dispatcher, types, executor
from config import token 

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Привет мир! Привет Geeks Python")

@dp.message_handler(commands='help')
async def help(message:types.Message):
    await message.answer("Чем я могу вам помочь?")

@dp.message_handler(text='Привет')
async def hello(message:types.Message):
    await message.answer("Привет, как дела?")

@dp.message_handler(commands='test')
async def test(message:types.Message):
    await message.reply('Тестовое сообщение')
    await message.answer_location(40.51933983835417, 72.80298453971301)
    await message.answer_dice()
    await message.answer_photo('https://i.ytimg.com/vi/jMm37VNFhLc/maxresdefault.jpg')
    await message.answer_contact('+996772343206', 'Kurmanbek', 'Toktorov')
    with open('photo.jpg', 'rb') as photo:
        await message.answer_photo(photo)

executor.start_polling(dp)