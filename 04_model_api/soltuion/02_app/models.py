from sqlalchemy import Column, Integer, DateTime, Float

from database import Base


class DataIn(Base):
    __tablename__ = "raw_data"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    sepal_width = Column(Float)
    sepal_length = Column(Float)
    petal_width = Column(Float)
    petal_length = Column(Float)


class DataOut(Base):
    __tablename__ = "prediction"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    iris_class = Column(Integer)
