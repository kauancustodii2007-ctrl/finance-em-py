from sqlalchemy.orm import Session
from app.models.expense import Expense

class ExpenseRepository:

    @staticmethod
    def create(db: Session, expense):
        db_expense = Expense(**expense.dict())
        db.add(db_expense)
        db.commit()
        db.refresh(db_expense)
        return db_expense

    @staticmethod
    def get_all(db: Session):
        return db.query(Expense).all()