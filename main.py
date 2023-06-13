import asyncio
import logging
import time
from enum import Enum
from pathlib import Path

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import AllowedUpdates
from mutagen.id3 import ID3
from mutagen.mp3 import MP3

API_TOKEN = "5192324361:AAHoYk3Qa1vKHs8j7FWM0nJru4g274g3J-w"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
URL_REG: str = r"http[s]*?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b[-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*[\/]*"


class Extension(Enum):
    mp3 = ".mp3"


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message) -> None:
    ...


@dp.message_handler(regexp=URL_REG)
async def handle_links(message: types.Message) -> None:
    ...


class Middleware(BaseMiddleware):
    """
    Simple middleware
    """

    async def on_process_message(self, message: types.Message, data: dict):
        """
        This handler is called when dispatcher receives a message

        :param message:
        """
        ...

    async def on_process_update(self, update: types.Update, data: dict):
        if (audio := update.message.audio) and Path(audio.file_name).suffix == Extension.mp3.value:
            file = await audio.download()
            # audio = MP3(file.name)
            # id3_1 = ID3(file.name)
            # print(id3_1)
            # audio.delete()
            # audio.save()
            # id3_2 = ID3(file.name)
            # print(id3_2)
        ...


async def main():
    dp.middleware.setup(Middleware())
    await dp.start_polling(allowed_updates=AllowedUpdates.all())

if __name__ == "__main__":
    asyncio.run(main())
