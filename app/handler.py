from telegram import Update
from telegram.ext import ContextTypes

from app.main import main_cost
from app.user.model.query_handlers import access_query_handler


async def callback_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_data = context.chat_data

    if 'app' in chat_data.keys() and not chat_data['app'] == '':
        if chat_data['app'] == 'user':
            if chat_data['state'] == 'insert_wait_for_accept':
                await access_query_handler(update, context)
        elif chat_data['app'] == 'main_app':
            query = update.callback_query
            data = str(query.data)

            if data == 'cost':
                await main_cost(update, context)
