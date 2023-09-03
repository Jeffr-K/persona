from sqlalchemy import Column, Integer, String, CHAR

from src.main import Base


class Users(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(40))
    gender = Column(CHAR(2))
    age = Column(Integer())
