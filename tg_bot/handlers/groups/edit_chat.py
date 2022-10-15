import io

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command

from tg_bot.filters.group import IsGroup


async def set_chat_photo(message: types.Message):
    source_message = message.reply_to_message.photo[-1]
    photo = await source_message.download(destination_file=io.BytesIO())
    input_file = types.InputFile(path_or_bytesio=photo)
    await message.chat.set_photo(photo=input_file)


async def set_chat_title(message: types.Message):
    title = message.reply_to_message.text
    await message.chat.set_title(title)


async def set_chat_description(message: types.Message):
    description = message.reply_to_message.text
    await message.chat.set_description(description)


def register_edit_chat_handlers(dp: Dispatcher):
    dp.register_message_handler(set_chat_photo, Command("set_photo", prefixes="!/"), IsGroup())
    dp.register_message_handler(set_chat_title, Command("set_title", prefixes="!/"), IsGroup())
    dp.register_message_handler(set_chat_description, Command("set_description", prefixes="!/"), IsGroup())
