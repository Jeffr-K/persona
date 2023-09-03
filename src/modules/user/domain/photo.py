from sqlalchemy import Column, Integer, String, CHAR

from src.main import Base


class Photo(Base):
    __tablename__ = "Photo"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(40))
    gender = Column(CHAR(2))
    age = Column(Integer())


Base.metadata.create_all(engine)