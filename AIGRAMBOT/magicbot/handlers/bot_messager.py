from aiogram import Router, F
from aiogram.types import Message

from keyboards import reply, inline, fabrics  # type: ignore

router = Router()


@router.message()
async def echo(message: Message):
    msg = message.text.lower()

    if msg == "мероприятия":
        await message.answer(f'photos{0}', reply_markup=F.paginator())

    elif msg == "последние эфиры":
        await message.answer("Вот ссылка на последний эфир:", reply_markup=inline.links_kb())

    elif msg == "забрать подарок":
        await message.answer_animation(animation="CAACAgIAAxkBAAMSZmSSGwc8Y2v_geE8ic7v5A-CdxYAAqMrAAIdKEBIrBAw6"
                                                 "-9ITVE1BA", caption="Подарок", show_caption_above_media=True)
