import asyncio
from aiogram import Bot, Dispatcher

from handlers import bot_messages, user_commands, questionaire  # type: ignore
from callbacks import pagination  # type: ignore


async def main():
    bot = Bot(token="7135356147:AAFXrTS-s_pXHtbTWg2djThFCy3rcr0pexs")
    dp = Dispatcher()

    dp.include_routers(
        user_commands.router,
        pagination.router,
        questionaire.router,
        bot_messages.router
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
