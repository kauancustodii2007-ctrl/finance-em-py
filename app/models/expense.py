from sqlalchemy import Column, Integer, String, Float
from app.database.connection import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    value = Column(Float)
    category = Column(String(50))
    date = Column(String(20))