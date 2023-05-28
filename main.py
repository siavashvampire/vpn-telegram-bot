from telegram.ext import Application, MessageHandler, filters, CallbackQueryHandler

from app.main import main_app
from app.start.main import start_new_user, start_exist_user, say_start_user
from app.handler import callback_query_handler
from app.user.main import without_access_user
from core.config.database import get_database
from core.custom_filter.custom_filter import user_exist_filter, access_filter
from core.error_handler.error import error_handler

application = Application.builder().token(token=get_database('telegram_token')).build()

application.add_handler(MessageHandler(filters.COMMAND & filters.Regex("start") & ~user_exist_filter, start_new_user))
application.add_handler(MessageHandler(filters.COMMAND & filters.Regex("start") & user_exist_filter, start_exist_user))
application.add_handler(MessageHandler(~user_exist_filter, say_start_user))

application.add_handler(MessageHandler(~access_filter & user_exist_filter, without_access_user))

application.add_handler(MessageHandler(access_filter, main_app))

application.add_handler(CallbackQueryHandler(callback_query_handler))

application.add_error_handler(error_handler)

# on non command i.e message - echo the message on Telegram
# application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
# application.add_handler(MessageHandler(user_exist_filter(), echo))
# application.add_handler(MessageHandler(~user_exist_filter(), echo2))

if __name__ == '__main__':
    from core.database.database import create_db

    create_db()

    application.run_polling()
