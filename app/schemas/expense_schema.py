from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    name: str
    value: float
    category: str
    date: str