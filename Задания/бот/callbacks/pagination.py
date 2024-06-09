from contextlib import suppress

from aiogram.types import FSInputFile

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from keyboards import fabrics  # type: ignore

router = Router()


img1 = FSInputFile(f'photos/0.png')
img2 = FSInputFile(f'photos/1.png')
img3 = FSInputFile(f'photos/2.png')
img4 = FSInputFile(f'photos/3.png')
photos =[img1, img2, img3, img4]
@router.callback_query(fabrics.Pagination.filter(F.action.in_(["prev", "next"])))  # type: ignore
async def pagination_handler(callback: CallbackQuery, callback_data: fabrics.Pagination):
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0


    if callback_data.action == "next":
        page = page_num + 1 if page_num < (len(photos) - 1) else page_num
    print(page)

    image = FSInputFile(f'photos/{page}.png')
    with suppress(TelegramBadRequest):
        await callback.bot.send_photo(chat_id=callback.from_user.id, photo=image, caption=f'photos{page}',
                                      reply_markup=fabrics.paginator(page))
    await callback.answer()
