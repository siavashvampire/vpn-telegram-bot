from app.pyxui.model.xui import XUI
from app.pyxui.errors.main import BadLogin
from core.config.database import xui_user_name, xui_password

xui = XUI("no.doiteasyy.online", 8530)

user_name = xui_user_name
password = xui_password

try:
    xui.login(user_name, password)
except BadLogin as e:
    print(e)

