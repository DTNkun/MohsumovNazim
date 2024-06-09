import asyncio
from aiogram import Bot, Dispatcher

from handlers import bot_messager, user_commands, questionaire  # type: ignore
from callbacks import pagination  # type: ignore


async def main():
    bot = Bot("7302792360:AAFDF2LdvryqL8WNmbeJkB9iVivR060uuFU")
    dp = Dispatcher()

    dp.include_routers(
        bot_messager.router,
        user_commands.router,
        pagination.router,
        questionaire.router

    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
