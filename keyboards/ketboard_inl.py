from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder




def menu_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    kb_builder.row(*[InlineKeyboardButton(
        text=button,
        callback_data=button) for button in buttons], width=1)

    # Добавляем в конец клавиатуры кнопку "Отменить"
    kb_builder.row(InlineKeyboardButton(
        text='отменить',
        callback_data='cancel'))

    return kb_builder.as_markup()


# Кнопка отмены
def cancel():
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(InlineKeyboardButton(
        text='отменить(в главное меню)',
        callback_data='cancel'))
    return kb_builder.as_markup()


def main_menu_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    kb_builder.row(*[InlineKeyboardButton(
        text=button,
        callback_data=button) for button in buttons], width=1)

    return kb_builder.as_markup()
