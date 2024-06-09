from aiogram import Router
from aiogram.types import Message
from keyboards import reply, inline, fabrics  # type: ignore

router = Router()


@router.message()
async def echo(message: Message):
    msg = message.text.lower()

    if msg == "актуальные мероприятия":
        await message.answer(f'photos{0}', reply_markup=fabrics.paginator())

    elif msg == "последние эфиры":
        await message.answer("Вот ссылка на последний эфир:", reply_markup=inline.links_kb)

    elif msg == "забрать подарок":
        await message.answer_animation( animation="CAACAgIAAxkBAAEF_4FmZGZeDMH0qyuq-G_l3SZSLqzeRgAC-yMAApMlWUkkh_JZ1Mma6DUE",caption="Подарок", show_caption_above_media=True)
