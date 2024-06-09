from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Актуальные мероприятия"),
            KeyboardButton(text="Последние эфиры"),
        ],
        [
            KeyboardButton(text="Забрать подарок"),
        ]
    ],
    resize_keyboard=True
)

rmk = ReplyKeyboardRemove()