from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.mongo import MongoStorage

from motor.motor_asyncio import AsyncIOMotorClient

import asyncio
import os

mongo_client = AsyncIOMotorClient(os.getenv('MONGO_DB'))

bot = Bot(token=os.getenv('BOT_TOKEN'))
dispatcher = Dispatcher(storage=MongoStorage(
    client=mongo_client,
    db_name='aiogram_fsm',
    collection_name='fsm_data'
))

def include_routers():
    from commands import start

    dispatcher.include_router(start.router)

async def main():
    include_routers()

    await dispatcher.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())