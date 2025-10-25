from aiogram.filters import CommandObject, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router

from utm.gateway import process_utm

router = Router()

@router.message(Command('start'))
async def start(message: Message, command: CommandObject, state: FSMContext):
    if command.args:
        await process_utm(message, command.args, state)
        return

    await message.answer("🔧 Maintaining is in progress...")
    return