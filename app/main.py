from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database.connection import Base, engine
from app.routes.expense_routes import router as expense_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Finance Manager",
    version="1.0.0",
    description="Sistema financeiro com FastAPI"
)

app.include_router(expense_router, prefix="/api", tags=["Expenses"])

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request}
    )

@app.get("/health")
def health():
    return {"status": "online"}
