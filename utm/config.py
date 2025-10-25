from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from abc import ABC, abstractmethod
from typing import List

class DefaultUtm(ABC):
    @classmethod
    @abstractmethod
    async def process(cls, message: Message, arg_data: List[str], ctx: FSMContext): pass
