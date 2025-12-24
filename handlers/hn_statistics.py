from aiogram import Router, F, types

from lexicon.lexicon_statistics import statistics

router: Router = Router()

@router.message(F.text == "📊 Статистика")
async def name_mess(message: types.Message):

    await message.answer(text=statistics)