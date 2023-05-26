from app.pyxui.methods.base import Base
from app.pyxui.methods.login import Login
from app.pyxui.methods.inbounds import Inbounds
from app.pyxui.methods.clients import Clients


class Methods(
    Base,
    Login,
    Inbounds,
    Clients
):
    pass
