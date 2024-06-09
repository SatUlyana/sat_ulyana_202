from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    name = State()
    nickname = State()
    email = State()
    phone = State()
