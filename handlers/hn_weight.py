from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from keyboards.ketboard_inl import menu_keyboard
from lexicon.lexicon_weight import dyinamics, weight_rec, weight_save, button1w
from services.sv_registration import calculate_calories
from services.sv_weight import calculate_weight

router: Router = Router()

class FSMFillForm(StatesGroup):

    fill_rec = State()


@router.message(F.text == "⚖ Вес")
async def name_mess(message: types.Message, state: FSMContext):

    await message.answer(text=dyinamics, reply_markup=menu_keyboard(*button1w))


@router.callback_query(F.data == "📝 Записать текущий вес")
async def gender_callback(callback: types.CallbackQuery, state: FSMContext):

    await callback.message.edit_text(text=weight_rec)
    await state.set_state(FSMFillForm.fill_rec)

@router.message(StateFilter(FSMFillForm.fill_rec))
async def birthday_mess(message: types.Message, state: FSMContext):
    #await state.update_data(new_weight=message.text)
    dict_weight = await calculate_weight(message.text)
    text = weight_save.format(today=dict_weight['today'], new_w=dict_weight['new_w'],
                              target=dict_weight['target'], last_change=dict_weight['last_change'],
                              all_change=dict_weight['all_change'],
                              target_change=dict_weight['target_change'])
    await message.answer(text=text)


@router.callback_query(F.data == "📅 История измерений")
async def gender_callback(callback: types.CallbackQuery):
    pass


@router.callback_query(F.data == "📈 График изменений")
async def gender_callback(callback: types.CallbackQuery):
    pass

@router.callback_query(F.data == "🎯 Установить цель")
async def gender_callback(callback: types.CallbackQuery, state: FSMContext):
    pass


@router.callback_query(F.data == "↩️ Назад в меню")
async def gender_callback(callback: types.CallbackQuery):
    pass