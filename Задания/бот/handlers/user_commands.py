from aiogram import Router
from aiogram import types, F
from aiogram.types import Message
from aiogram.filters.command import Command

from keyboards import reply  # type: ignore


router = Router()

@router.message(Command("start")) 
async def cmd_start(message: types.Message):
    await message.answer("Hello!Вас приветствует бот fairytail! Для начала пройдите регистрацию (/profile). ", reply_markup=reply.main_kb)