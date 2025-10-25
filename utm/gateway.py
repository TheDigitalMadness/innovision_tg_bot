from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from enum import Enum

from utm.scanned_code import ScannedCodeUtm

class CommandType(str, Enum):
    scanned_code = 'scanned-code'

class Messages(str, Enum):
    not_recognized = '❌ Ошибка в аргументах команды!'

async def process_utm(message: Message, args: str, ctx: FSMContext):
    args = args.strip().split('_')

    arg_type = args[0]
    arg_data = args[1:]

    match arg_type:
        case CommandType.scanned_code:
            await ScannedCodeUtm.process(message, arg_data, ctx)
        case _:
            await message.answer(Messages.not_recognized)