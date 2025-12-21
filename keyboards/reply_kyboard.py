from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon.lexicon_ru import main_menu

keyboard = [[KeyboardButton(text=main_menu[(j-1)*2 + i]) for i in range(2)] for j in range(3)]

# Создаем объект клавиатуры, добавляя в него кнопки
menu_keyboard_g = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True
)