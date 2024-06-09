from aiogram import Router
from aiogram import types, F
from aiogram.types import Message
from aiogram.filters.command import Command

from keyboards import reply  # type: ignore


router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать в искусство. ", reply_markup=reply.main_kb)