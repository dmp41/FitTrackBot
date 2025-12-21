
from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from keyboards.ketboard_inl import menu_keyboard
from keyboards.reply_kyboard import menu_keyboard_g
from lexicon.lexicon_ru import name, gender, button2, birthday, height, weight, target, button3, activity, button4, \
    calories, button5, greetings

router: Router = Router()

class FSMFillForm(StatesGroup):
    fill_name = State()
    fill_gender = State()
    fill_birthday = State()
    fill_height = State()
    fill_weight = State()
    fill_target = State()
    fill_activity = State()
    fill_calories = State()

@router.callback_query(F.data == "✅ Начать с бесплатной версии")
async def enter_free_callback(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text=name)
    await state.set_state(FSMFillForm.fill_name)

@router.message(StateFilter(FSMFillForm.fill_name))
async def name_mess(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text=gender, reply_markup=menu_keyboard(*button2))
    await state.set_state(FSMFillForm.fill_gender)


@router.callback_query(StateFilter(FSMFillForm.fill_gender),
                   F.data.in_(button2))
async def gender_callback(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(gender=callback.data)
    await callback.message.edit_text(text=birthday)
    await state.set_state(FSMFillForm.fill_birthday)

@router.message(StateFilter(FSMFillForm.fill_birthday))
async def birthday_mess(message: types.Message, state: FSMContext):
    await state.update_data(birthday=message.text)
    await message.answer(text=height)
    await state.set_state(FSMFillForm.fill_height)

@router.message(StateFilter(FSMFillForm.fill_height))
async def height_mess(message: types.Message, state: FSMContext):
    await state.update_data(height=message.text)
    await message.answer(text=weight)
    await state.set_state(FSMFillForm.fill_weight)

@router.message(StateFilter(FSMFillForm.fill_weight))
async def weight_mess(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    await message.answer(text=target, reply_markup=menu_keyboard(*button3))
    await state.set_state(FSMFillForm.fill_target)

@router.callback_query(StateFilter(FSMFillForm.fill_target),
                   F.data.in_(button3))
async def weight_mess(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(target=callback.data)
    await callback.message.edit_text(text=activity, reply_markup=menu_keyboard(*button4))
    await state.set_state(FSMFillForm.fill_activity)

@router.callback_query(StateFilter(FSMFillForm.fill_activity),
                   F.data.in_(button4))
async def weight_mess(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(activity=callback.data)
    await callback.message.edit_text(text=calories, reply_markup=menu_keyboard(*button5))
    await state.set_state(FSMFillForm.fill_calories)


@router.callback_query(StateFilter(FSMFillForm.fill_calories),
                   F.data.in_(button5))
async def weight_mess(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(calories=callback.data)
    await callback.message.answer(text=greetings, reply_markup=menu_keyboard_g)
    #await state.set_state(FSMFillForm.fill_calories)


