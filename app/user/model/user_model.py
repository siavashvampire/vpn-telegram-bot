from sqlalchemy import Column, String, Integer, BigInteger, DateTime, Boolean
from telegram import User

from core.config.database import bot_admin_id
from core.database.Base import Base
from core.database.database import session
from datetime import datetime


class UserDB(User, Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    id = Column(BigInteger, primary_key=True, unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50))
    access = Column(Boolean, default=0)
    insert_time = Column(DateTime, default=datetime.now)

    def __init__(self, id: int = 0, username: str = "", first_name: str = "", last_name: str = "") -> None:
        self._frozen = False

        try:
            temp: UserDB = session.query(UserDB).filter(UserDB.id == id).first()
            if temp is None:
                raise AttributeError

            self.id = temp.id
            self.user_id = temp.user_id
            self.first_name = temp.first_name
            self.last_name = temp.last_name
            self.username = temp.username
            self.access = temp.access
        except:
            self.id = id
            self.first_name = first_name
            self.last_name = last_name
            self.username = username
            self.username = 0

        User.__init__(self=self, id=id, first_name=first_name, last_name=last_name, is_bot=False, username=username)
        Base.__init__(self)

    def insert_user(self) -> bool:
        temp: UserDB = session.query(UserDB).filter(UserDB.id == self.id).first()
        if temp is not None:
            return False
        try:
            session.add(self)
            session.commit()
            return True
        except:
            return False

    def check_exist_user(self) -> bool:
        temp: UserDB = session.query(UserDB).filter(UserDB.id == self.id).first()
        if temp is not None:
            return True
        return False

    def check_admin(self) -> bool:
        return self.id in bot_admin_id

    def check_access(self) -> bool:
        return self.access

    def change_access(self, cond: int) -> None:
        self._frozen = False
        self.access = cond

    def __repr__(self):
        return "<User(%r, %r)>" % (self.first_name, self.id)

    # def set_user_to_user_data(self,context: CallbackContext):
    #     user = get_user(id_in=self.id)
    #     user_data = context.user_data
    #     user_data['user'] = user
    #     user_data['user_id'] = user.user_id
    #     user_data['id'] = user.id
    #     user_data['first_name'] = user.first_name
    #     user_data['last_name'] = user.last_name
    #     user_data['username'] = user.username
    #     user_data['user_physics_user'] = user.user_physics_user
    #     user_data['user_physics_work_user'] = user.user_physics_work_user
    #     user_data['is_admin_flag'] = user.check_admin()
