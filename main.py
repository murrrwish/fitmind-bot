from vkbottle import Bot, Message

import os

TOKEN = os.getenv("VK_TOKEN")

bot = Bot(token=TOKEN)

@bot.on.message(text="/start")

async def start_handler(message: Message):

    await message.answer(

        "Привет! Я Fitmind 💪\n\n"

        "Выбери, что хочешь сделать:\n"

        "1. Рассчитать КБЖУ\n"

        "2. План тренировок\n"

        "3. План питания\n"

        "4. Загрузить InBody"

    )

@bot.on.message()

async def handle(message: Message):

    text = message.text.lower()

    if "кбжу" in text:

        await message.answer("Введи: вес, рост, возраст")

    elif "трен" in text:

        await message.answer("Сколько раз в неделю хочешь тренироваться?")

    elif "питан" in text:

        await message.answer("Сейчас составлю тебе план питания...")

    elif "inbody" in text:

        await message.answer("Отправь фото анализа")

    else:

        await message.answer("Напиши /start чтобы начать")

bot.run_forever()
