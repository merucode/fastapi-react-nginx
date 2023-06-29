from sqlalchemy import Column, String, Date, JSON, BIGINT, Integer, REAL

from database import Base

class WordsCount(Base):
    __tablename__ = "words_count_table"

    date = Column(Date, nullable=False, primary_key=True)
    words_count = Column(JSON, nullable=False)
    code = Column(String, nullable=False)


class StockOHLCV(Base):
    __tablename__ = "stock_table"

    date = Column(Date, nullable=False, primary_key=True)
    open = Column(Integer, nullable=False)
    high = Column(Integer, nullable=False)
    low = Column(Integer, nullable=False)
    close = Column(Integer, nullable=False)
    volume = Column(BIGINT, nullable=False)
    code = Column(String, nullable=False)


class IndexOHLCV(Base):
    __tablename__ = "index_table"

    date = Column(Date, nullable=False, primary_key=True)
    open = Column(REAL, nullable=False)
    high = Column(REAL, nullable=False)
    low = Column(REAL, nullable=False)
    close = Column(REAL, nullable=False)
    volume = Column(BIGINT, nullable=False)
    code = Column(String, nullable=False)



