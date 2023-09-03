from sqlalchemy import Column, Integer

from src.main import Base


class Persona(Base):
    __tablename__ = "Persona"

    id = Column(Integer, primary_key=True, index=True)
