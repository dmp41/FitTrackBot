from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.ketboard_inl import main_menu_keyboard
from keyboards.reply_kyboard import menu_keyboard_g
from lexicon.lexicon_ru import button1, after_start_description
from aiogram.fsm.context import FSMContext

router: Router = Router()

@router.message(CommandStart())
async def admin_check_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text= after_start_description,
        reply_markup=main_menu_keyboard(*button1)
    )
    #await message.answer(
     #   text='меню',
        #reply_markup=menu_keyboard
    #)
    #await UsersService(db).add_user(
     #   tg_id=message.from_user.id,
      #  username=message.from_user.username,
      #  first_name=message.from_user.first_name,
       # last_name=message.from_user.last_name
    #)