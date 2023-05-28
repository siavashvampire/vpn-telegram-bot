from sqlalchemy import Column, String, Integer

from core.database.Base import Base
from core.database.database import session


class CostModel(Base):
    __tablename__ = 'cost'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(50))
    expired_day = Column(Integer)
    total_gb = Column(Integer)
    cost = Column(Integer)

    def __init__(self, id: int = 0, name: str = "") -> None:
        try:
            if id != 0:
                temp: CostModel = session.query(CostModel).filter(CostModel.id == id).first()
            elif name != "":
                temp: CostModel = session.query(CostModel).filter(CostModel.name == name).first()
            else:
                raise

            self.id = temp.id
            self.name = temp.name
            self.expired_day = temp.expired_day
            self.total_gb = temp.total_gb
            self.cost = temp.cost
        except:
            self.id = 0
            self.name = ""
            self.expired_day = 0
            self.total_gb = 0
            self.cost = 0

        Base.__init__(self)

    def __repr__(self):
        return "<Cost(%r, %r, %r, %r)>" % (self.name, self.expired_day, self.total_gb,self.cost)

    def insert(self) -> bool:
        try:
            session.add(self)
            session.commit()
            return True
        except:
            return False
