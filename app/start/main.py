from time import sleep
from telegram import Update, Message
from telegram.ext import ContextTypes

from app.user.api import add_user
from core.config.database import bot_admin_id
from core.markups.markup import get_user_accept_reject_markup


async def start_new_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.deleteMessage(chat_id=update.effective_message.chat.id, message_id=update.effective_message.id)

    user = update.effective_message.from_user

    # noinspection PyTypeChecker
    temp_message: Message = await update.effective_message.reply_text(
        "سلام " + user.first_name + ", به ممد خوش اومدی 🫡🌸")

    flag = add_user(user)
    sleep(2)

    await context.bot.deleteMessage(chat_id=update.effective_message.chat.id, message_id=temp_message.id)

    if flag:
        chat_data = context.chat_data
        chat_data['app'] = 'user'
        chat_data['state'] = 'insert_wait_for_accept'
        await update.effective_message.reply_text("You have been added to mamad users correctly")

        await update.effective_message.reply_text("we send your user to admin for checking access")


        # await update.effective_message.reply_html(
        #     rf"you dont have access to bot plz contact {admin_user.mention_html()} to give you access")

        await context.bot.send_message(bot_admin_id[0],
                                       "user with first name " + user.first_name + "\n user = @" + user.username,
                                       reply_markup=get_user_accept_reject_markup(user.id))
    else:
        await update.effective_message.reply_text("Sorry ,we cant add you to mamad users")


async def start_exist_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.deleteMessage(chat_id=update.effective_message.chat.id, message_id=update.effective_message.id)
    user = update.effective_message.from_user

    # noinspection PyTypeChecker
    temp_message: Message = await update.effective_message.reply_text(
        "Hello " + user.first_name + ", Welcome to the mamad")

    sleep(1)
    await context.bot.deleteMessage(chat_id=update.effective_message.chat.id, message_id=temp_message.id)

    await update.effective_message.reply_text("your already are mamad user")


async def say_start_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.effective_message.reply_text("please start bot with /start command")
