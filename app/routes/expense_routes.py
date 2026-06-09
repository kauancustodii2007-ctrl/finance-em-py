from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.expense_schema import ExpenseCreate
from app.services.expense_service import ExpenseService

router = APIRouter()

@router.post("/expenses")
def create_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db)
):
    return ExpenseService.create_expense(db, expense)

@router.get("/expenses")
def list_expenses(
    db: Session = Depends(get_db)
):
    return ExpenseService.list_expenses(db)