from sqlalchemy import Column, String, Date, JSON

from database import Base

class WordsCount(Base):
    __tablename__ = "test_table"

    date = Column(Date, nullable=False, primary_key=True)
    words_count = Column(JSON, nullable=False)
    code = Column(String, nullable=False)
