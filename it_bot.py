from aiogram import Bot, Dispatcher, types, executor
from logging import basicConfig, INFO
from config import token 

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)

start_buttons = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('Контакты'),
    types.KeyboardButton('Курсы')
]
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Привет, добро пожаловать в курсы Geeks!", reply_markup=start_keyboard)

@dp.message_handler(text="О нас")
async def about_us(message:types.Message):
    await message.answer("Geeks - это айти курсы в Бишкеке, Кара-Балте и Оше созданное в 2019 году")

@dp.message_handler(text="Адрес")
async def address(message:types.Message):
    await message.reply("Наш адрес:\nМырзалы Аматова 1Б (БЦ Томирис)")
    await message.answer_location(40.519295524301064, 72.80298073930457)

@dp.message_handler(text="Контакты")
async def contact(message:types.Message):
    await message.answer("Наши контакты:")
    await message.answer_contact("+996777123123", "Nurbolot", "Erkinbaev")
    await message.answer_contact("+996777123120", "Ulan", "Ashirov")

courses_buttons = [
    types.KeyboardButton("Backend"),
    types.KeyboardButton("Frontend"),
    types.KeyboardButton("iOS"),
    types.KeyboardButton("Android"),
    types.KeyboardButton("UX/UI"),
    types.KeyboardButton("Назад")
]
courses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*courses_buttons)

@dp.message_handler(text="Курсы")
async def courses(message:types.Message):
    await message.answer("Вот наши курсы:", reply_markup=courses_keyboard)

@dp.message_handler(text="Backend")
async def backend(message:types.Message):
    await message.answer("Backend - это серверная сторона приложения или сайта, которую мы не видим")

@dp.message_handler(text="Frontend")
async def frontend(message:types.Message):
    await message.answer("Frontend - это лицевая стороная сайта, которую мы можем видеть своими глазами")

@dp.message_handler(text="iOS")
async def ios(message:types.Message):
    await message.answer("iOS - это операционная система на мобильных устройствах компании Apple")

@dp.message_handler(text="Android")
async def anndroid(message:types.Message):
    await message.answer("Android - это популярная операционная система, которую используют многие компании")

@dp.message_handler(text="UX/UI")
async def uxui(message:types.Message):
    await message.answer("UX/UI - это дизайн сайта или приложения")

@dp.message_handler(text="Назад")
async def cancell(message:types.Message):
    await start(message)

executor.start_polling(dp)