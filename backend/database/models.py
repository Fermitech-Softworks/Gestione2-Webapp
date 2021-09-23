from sqlalchemy import Integer, String, LargeBinary, Column, Boolean, ForeignKey, SmallInteger, DateTime
from sqlalchemy.orm import relationship
from backend.database.schemas import User as UserSchema

from backend.database.db import Base


class User(Base):
    __tablename__ = "user"

    uid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(LargeBinary, nullable=False)
    isAdmin = Column(Boolean, default=True)

    def to_schema(self):
        return UserSchema(uid=self.uid, name=self.name, surname=self.surname, email=self.email)
