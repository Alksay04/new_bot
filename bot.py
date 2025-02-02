import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from dotenv import dotenv_values
from menu.menu import meal_container

config = dotenv_values()

bot = Bot(token=config['TOKEN'])
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message):
    await message.reply('Привет')
    for meal in meal_container.meals:
        await message.reply(str(meal))

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
    