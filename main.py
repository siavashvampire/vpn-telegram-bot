from pyrogram import Client

from core.config.database import get_database

proxy = {
    "scheme": "http",  # "socks4", "socks5" and "http" are supported
    "hostname": "172.27.77.121",
    "port": 8082
}

plugins = dict(root="app")

app = Client(name=get_database("telegram_bot_name"),
             api_id=get_database("telegram_api_id"),
             api_hash=get_database("telegram_api_hash"),
             bot_token=get_database('telegram_token'),
             plugins=plugins,
             # proxy=proxy
             )

if __name__ == '__main__':
    from core.database.database import create_db

    create_db()

    app.run()
