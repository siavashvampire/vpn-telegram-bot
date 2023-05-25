from pyrogram import filters,Client
from pyrogram.types import Message

from app.user.api import check_exist_user


def dynamic_data_filter(data):
    async def func(flt, _, query):
        return flt.data in query.data

    return filters.create(func, data=data)


async def user_exist_filter(_, client: Client, message: Message):
    return check_exist_user(message.from_user)


user_exist_filter = filters.create(user_exist_filter)