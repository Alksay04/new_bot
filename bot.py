import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import StateFilter
from aiogram.filters.command import Command
from dotenv import dotenv_values
from menu.menu import meal_container
from keyboards import menu_keyboard

config = dotenv_values()

bot = Bot(token=config['TOKEN'])
dp = Dispatcher()

@dp.message(StateFilter(None), Command('start'))
async def cmd_start(message, state):
    await message.reply('Привет, выбери блюдо:',
                        reply_markup=menu_keyboard(meals_list=meal_container))
    for meal in meal_container.meals:
        await message.reply(str(meal))

    await state.set_state(OrderStates.choosing_meal)
    await state.set_data('total': 0)

@dp.callback_query(F.data.startwith('meal_'))
async def test_callback(callback):
    data = callback.data.split('_')[-1]
    meal = meal_container.get_meal_by_id(int(data))
    await callback.message.reply(f'Вы заказали: {meal.name}')



async def main():
    await dp.start_polling(bot)

asyncio.run(main())
    