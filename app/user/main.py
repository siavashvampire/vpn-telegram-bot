from telegram import Update, Message
from telegram.ext import ContextTypes

from app.user.api import get_user
from core.config.database import bot_admin_id


async def without_access_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    admin_user = get_user(id_in=bot_admin_id[0])

    await update.effective_message.reply_html(
        rf"you dont have access to bot plz contact {admin_user.mention_html()} to give you access")
