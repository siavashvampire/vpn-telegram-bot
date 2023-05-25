from pathlib import Path

from tinydb import TinyDB

dev = True
path = '../../File/config//config.json'

parent_path = Path(__file__).resolve().parent
db_path = parent_path.joinpath(path).resolve()

db = TinyDB(db_path)
db.drop_tables()
table = db.table('config')

if dev:
    table.insert({'telegram_token': "5911882360:AAFQABCYQXObbISk4BGe4DE-_Vtxn39uQ1I"})
else:
    table.insert({'telegram_token': "5911882360:AAFQABCYQXObbISk4BGe4DE-_Vtxn39uQ1I"})

table.update({'telegram_api_id': 28040203})
table.update({'telegram_bot_name': "siavash_test_comp_462_bot"})
table.update({'telegram_api_hash': "a6189bef475420246532e6f0a66839c5"})

table.update({'bot_admin_id': [99981475]})

print('file successfully make at ' + str(db_path))
