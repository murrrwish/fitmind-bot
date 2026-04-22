from vkbottle import Bot, Message

import os

from flask import Flask

import threading

TOKEN = os.getenv("VK_TOKEN")

bot = Bot(token=TOKEN)

app = Flask(__name__)

@bot.on.message(text="/start")

async def start_handler(message: Message):

    await message.answer("Привет! Я Fitmind 💪")

@bot.on.message()

async def handle(message: Message):

    await message.answer("Я работаю 😎")

# фейковый сервер (важно!)

@app.route("/")

def home():

    return "Bot is running!"

def run_bot():

    bot.run_forever()

if name == "__main__":

    threading.Thread(target=run_bot).start()

    app.run(host="0.0.0.0", port=10000)
