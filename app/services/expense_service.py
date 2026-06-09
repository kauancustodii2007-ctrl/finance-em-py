from app.repositories.expense_repository import ExpenseRepository

class ExpenseService:

    @staticmethod
    def create_expense(db, expense):
        return ExpenseRepository.create(db, expense)

    @staticmethod
    def list_expenses(db):
        return ExpenseRepository.get_all(db)