from typing import Union

from tinydb import TinyDB, Query

path = 'File/config/config.json'

db = TinyDB(path)
query = Query()
table = db.table('config')

data = table.all()
data_all = None

if len(data):
    data_all = data[0]
else:
    raise ValueError('config database not set!please run make config!!')

telegram_token: str = data_all['telegram_token']
bot_admin_id: list[int] = data_all['bot_admin_id']
telegram_api_id: int = data_all['telegram_api_id']
telegram_bot_name: str = data_all['telegram_bot_name']
telegram_api_hash: str = data_all['telegram_api_hash']
xui_user_name: str = data_all['xui_user_name']
xui_password: str = data_all['xui_password']


def update_database(key: str, value: Union[int, float]) -> None:
    table.update({key: value})


def get_database(key: str):
    return data_all[key]
