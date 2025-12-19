

from aiogram import Router, F, types
from aiogram.types import Message

from keyboards.ketboard_inl import menu_keyboard

router: Router = Router()

@router.callback_query(F.data == "🍎 Питание")
async def enter_birth_date_callback(callback: types.CallbackQuery):
    await callback.message.answer('меню', reply_markup=menu_keyboard())


@router.callback_query(F.data == "⚖ Вес")
async def enter_birth_date_callback(callback: types.CallbackQuery):
    await callback.message.answer('меню', reply_markup=menu_keyboard())


@router.callback_query(F.data == "💪 Тренировка")
async def enter_birth_date_callback(callback: types.CallbackQuery):
    await callback.message.answer('меню', reply_markup=menu_keyboard())


@router.callback_query(F.data == "📊 Статистика")
async def enter_birth_date_callback(callback: types.CallbackQuery):
    await callback.message.answer('меню', reply_markup=menu_keyboard())


@router.callback_query(F.data == "⚙ Настройки")
async def enter_birth_date_callback(callback: types.CallbackQuery):
    await callback.message.answer('меню', reply_markup=menu_keyboard())


@router.callback_query(F.data == "ℹ Помощь")
async def enter_birth_date_callback(callback: types.CallbackQuery):
    await callback.message.answer('меню', reply_markup=menu_keyboard())

