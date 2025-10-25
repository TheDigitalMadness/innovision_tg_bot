from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from typing import List
from enum import Enum

from utm.config import DefaultUtm

class ScannedCodeTypes(str, Enum):
    demo = 'demo'
    prod = 'prod'

class UserTypes(str, Enum):
    student = 'student'
    teacher = 'teacher'

class Messages:
    not_recognized = '❌ Ошибка в аргументах команды!'

    class Demo(str, Enum):
        student = '✔ \n\nПодтверждено участие пользователя <b>John Lohhan</b> в кружке <b>"Increasing our results in computer science"</b>!'
        teacher = '✔ \n\nПодтверждено проведение пользователем <b>Nell Millian</b> кружка <b>"Increasing our results in computer science"</b>!'

class ScannedCodeUtm(DefaultUtm):
    @classmethod
    async def process(cls, message: Message, arg_data: List[str], ctx: FSMContext):
        scanned_code_type = arg_data[0]

        scanned_code_data = arg_data[1:]

        match scanned_code_type:
            case ScannedCodeTypes.demo:
                await cls.demo(message, scanned_code_data, ctx)
            case _:
                await message.answer(Messages.not_recognized)

    @staticmethod
    async def demo(message: Message, arg_data: List[str], ctx: FSMContext):
        async def student():
            await message.answer("💡 Это демонстрационный QR-код!")
            await message.answer(Messages.Demo.student, parse_mode=ParseMode.HTML)
            return

        async def teacher():
            await message.answer("💡 Это демонстрационный QR-код!")
            await message.answer(Messages.Demo.teacher, parse_mode=ParseMode.HTML)
            return

        user_type = arg_data[0]
        match user_type:
            case UserTypes.student:
                await student()
            case UserTypes.teacher:
                await teacher()
            case _:
                await message.answer(Messages.not_recognized)