from sqlalchemy import Column, Integer, String, Text, Date
from database import Base

class TestModel(Base):
    __tablename__ = "test_table"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    date = Column(Date, nullable=False)
    value = Column(Integer, nullable=False)
