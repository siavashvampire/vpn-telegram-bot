from telegram import Update
from telegram.ext import ContextTypes

from core.markups.markup import get_main_markup, get_cost_markup


async def main_app(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_data = context.chat_data
    chat_data['app'] = 'main_app'
    await update.effective_message.reply_html("welcome", reply_markup=get_main_markup())


async def main_cost(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_data = context.chat_data
    chat_data['app'] = 'main_app'
    chat_data['state'] = 'cost'
    await update.effective_message.reply_html("تعرفه ها", reply_markup=get_cost_markup())
