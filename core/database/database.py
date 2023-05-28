from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from core.database.Base import Base

user = 'Comp_462_siavash'
password = 'VamPire1468'
host = '127.0.0.1'
port = 3306
database = 'vpn_tele_bot'


def get_connection() -> Engine:
    return create_engine(
        url="mysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )


engine = get_connection()

session = sessionmaker(bind=engine)()


def create_db() -> None:
    from app.user.model.user_model import UserDB
    from app.logging.model.log_model import LogModel
    from app.cost.model.cost_model import CostModel

    UserDB()
    CostModel()
    LogModel()
    Base.metadata.create_all(engine)

    # session.add(ed_user)
