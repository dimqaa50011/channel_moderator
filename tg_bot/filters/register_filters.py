from aiogram import Dispatcher

from .admin import IsAdmin
from .group import IsGroup


def register_all_filters(dp: Dispatcher):
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory(IsGroup)
