from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, CHAR

app = FastAPI()

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://postgres:root@localhost:5432/persona_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Users(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(40))
    gender = Column(CHAR(2))
    age = Column(Integer())


Base.metadata.create_all(engine)


