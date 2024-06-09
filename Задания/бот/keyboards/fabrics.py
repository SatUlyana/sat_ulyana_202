from aiogram.types import InlineKeyboardButton  # type: ignore
from aiogram.utils.keyboard import InlineKeyboardBuilder # type: ignore
from aiogram.filters.callback_data import CallbackData # type: ignore


class Pagination(CallbackData, prefix="pag"):
    action: str 
    page: int 


def paginator(page: int=0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="←", callback_data=Pagination(action="prev", page=page).pack()),
        InlineKeyboardButton(text="→", callback_data=Pagination(action="next", page=page).pack()),
    )
    return builder.as_markup()