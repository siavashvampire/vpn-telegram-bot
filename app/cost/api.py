from app.cost.model.cost_model import CostModel
from core.database.database import session


def get_cost(id_in: int = 0, name: int = 0) -> CostModel:
    temp = CostModel()

    if id_in != 0:
        temp: CostModel = session.query(CostModel).filter(CostModel.id == id_in).first()
    elif name != "":
        temp: CostModel = session.query(CostModel).filter(CostModel.name == name).first()

    return temp


def add_cost(name: str) -> bool:
    temp = CostModel()
    temp.name = name
    return temp.insert()


def get_all_cost() -> list[CostModel]:
    return session.query(CostModel).all()
