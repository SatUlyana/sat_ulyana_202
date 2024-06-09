from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.states import Form  # type: ignore
from keyboards.builders import profile  # type: ignore
from keyboards.reply import rmk  # type: ignore

router = Router()


@router.message(Command("profile"))
async def fill_profile(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer(
        "Введите свое имя",
        reply_markup=profile(message.from_user.first_name)
    )


@router.message(Form.name)
async def form_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.nickname)
    await message.answer("Хорошо, теперь введите свой никнейм", reply_markup=rmk)


@router.message(Form.nickname)
async def form_nickname(message: Message, state: FSMContext):
    await state.update_data(nickname=message.text)
    await state.set_state(Form.email)
    await message.answer("Теперь введите свою почту", reply_markup=rmk)


@router.message(Form.email)
async def form_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await state.set_state(Form.phone)
    await message.answer("И номер телефона", reply_markup=rmk)


@router.message(Form.phone)
async def form_phone(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(phone=message.text)
    else:
        await message.answer("Введите числа!")
    await state.clear()
    await message.answer("Регистрация прошла успешно", reply_markup=rmk)
