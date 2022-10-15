from aiogram import Dispatcher

from .groups.edit_chat import register_edit_chat_handlers
from .users.admin import register_admin_hanlers
from .users.echo import register_echo_handler
from .users.start import register_start_handlers


def start_register_all_handlers(dp: Dispatcher):
    register_admin_hanlers(dp)
    register_start_handlers(dp)

    register_edit_chat_handlers(dp)

    register_echo_handler(dp)  # Эхо регистрировать самым последним
