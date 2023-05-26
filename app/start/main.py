from time import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from app.user.api import add_user
from core.pyrogram.custom_filter import user_exist_filter


@Client.on_message(filters.command("start") & ~user_exist_filter)
def start(client: Client, message: Message):
    client.delete_messages(message.chat.id, message.id)

    user = message.from_user

    # noinspection PyTypeChecker
    temp_message: Message = message.reply_text("Hello " + user.first_name + ", Welcome to the mamad")

    flag = add_user(user)
    sleep(1)
    client.delete_messages(chat_id=message.chat.id, message_ids=temp_message.id)
    if flag:
        message.reply_text("You have been added to mamad users correctly")
    else:
        message.reply_text("Sorry ,we cant add you to mamad users")


@Client.on_message(filters.command("start") & user_exist_filter)
def start(client: Client, message: Message):
    client.delete_messages(message.chat.id, message.id)

    user = message.from_user

    # noinspection PyTypeChecker
    temp_message: Message = message.reply_text("Hello " + user.first_name + ", Welcome to the mamad.")

    sleep(1)

    client.delete_messages(chat_id=message.chat.id, message_ids=temp_message.id)
    message.reply_text("your already are mamad user")
