from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from menu import meal_container

def menu_keyboard(meals_list, list: {str}):
    builder = InlineKeyboardBuilder()

    for meal in meals_list:
        builder.add(
            InlineKeyboardButton(text=meal, callback_data=f'meal_{meal_container.get_meal_by_name(meal).id}')
        )
    builder.adjust(3)
    return builder.as_markup()