from time import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from app.user.api import check_exist_user, add_user


@Client.on_message(filters.command("start"))
def start(client: Client, message: Message):
    client.delete_messages(message.chat.id, message.id)

    user = message.from_user

    # noinspection PyTypeChecker
    temp_message: Message = message.reply_text("Hello " + user.first_name + ", Welcome to the Comp 462.")

    flag = check_exist_user(user)

    if not flag:
        flag = add_user(user)
        sleep(1)
        client.delete_messages(chat_id=message.chat.id, message_ids=temp_message.id)
        if flag:
            message.reply_text("You have been added to Comp_462 users correctly")
            # set_user_to_user_data(update, context)
        else:
            message.reply_text("Sorry ,we cant add you to Comp_462 users")
    else:
        message.reply_text("your already are Comp_462 user")
        # set_user_to_user_data(update, context)

