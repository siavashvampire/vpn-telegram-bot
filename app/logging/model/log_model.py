from sqlalchemy import Column, Integer, ForeignKey,  DateTime
from sqlalchemy.orm import relationship

from core.database.Base import Base
from core.database.database import session
from datetime import datetime


class LogModel(Base):
    __tablename__ = 'log'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column(ForeignKey("users.user_id"))
    insert_time = Column(DateTime, default=datetime.now)

    user_rel = relationship("UserDB", foreign_keys=[user_id])

    def __init__(self, id: int = 0, user_id: int = 0, trading_id: int = 0, predict: int = 0) -> None:
        try:
            if id != 0:
                temp: LogModel = session.query(LogModel).filter(LogModel.id == id).first()
            else:
                raise

            self.id = temp.id
        except:
            self.id = 0
            self.user_id = user_id
            self.trading_id = trading_id
            self.predict = predict

        Base.__init__(self)

    def __repr__(self):
        if self.country_from_rel is not None:
            return "<Log(%r, %r)>" % (
                self.user_rel.first_name, self.id)
        else:
            return "<Log(%r, %r)>" % (
                self.user_id, self.id)

    def insert(self) -> bool:
        try:
            session.add(self)
            session.commit()
            return True
        except:
            return False
