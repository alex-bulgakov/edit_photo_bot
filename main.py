import asyncio
import os
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

from bot.handlers.user_handlers import register_user_handlers

logging.basicConfig(filename='app.log', level=logging.INFO)


def register_handler(dp: Dispatcher) -> None:
    register_user_handlers(dp)


async def main() -> None:
    load_dotenv()
    token = os.getenv('TOKEN')
    bot = Bot(token)
    dp = Dispatcher(bot)

    register_handler(dp)

    try:
        await dp.start_polling()
    except Exception as _ex:
        logging.error(_ex)


if __name__ == '__main__':
    asyncio.run(main())
