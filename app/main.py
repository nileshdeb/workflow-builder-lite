import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from .database import engine, Base, SessionLocal
from .models import RunHistory
from .workflow_engine import STEP_FUNCTIONS
import json
from sqlalchemy import text

Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# 🔹 HOME ROUTE
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    db = SessionLocal()
    runs = db.query(RunHistory).order_by(RunHistory.id.desc()).limit(5).all()

    return templates.TemplateResponse("index.html", {
        "request": request,
        "runs": runs
    })


# 🔹 RUN WORKFLOW
@app.post("/run", response_class=HTMLResponse)
def run_workflow(request: Request, text: str = Form(...), steps: list[str] = Form(...)):
    db: Session = SessionLocal()

    if not text.strip():
        runs = db.query(RunHistory).order_by(RunHistory.id.desc()).limit(5).all()

        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": "Input text cannot be empty",
            "runs": runs
        })

    current_text = text
    outputs = {}

    for step in steps:
        result = STEP_FUNCTIONS[step](current_text)

        # result is now dict {content, tokens, status}
        outputs[step] = result
        current_text = result["content"]

    # Save run in DB
    run = RunHistory(
        workflow_name="Custom Workflow",
        input_text=text,
        step_outputs=json.dumps(outputs)
    )

    db.add(run)
    db.commit()

    # Keep only last 5 runs
    runs = db.query(RunHistory).order_by(RunHistory.id.desc()).all()

    if len(runs) > 5:
        for r in runs[5:]:
            db.delete(r)
        db.commit()

    latest_runs = db.query(RunHistory).order_by(RunHistory.id.desc()).limit(5).all()

    return templates.TemplateResponse("index.html", {
        "request": request,
        "outputs": outputs,
        "runs": latest_runs
    })


# 🔹 STATUS PAGE (Improved Health Check)
@app.get("/status", response_class=HTMLResponse)
def status_page(request: Request):

    db_status = "Connected"
    llm_status = "Configured"

    # 🔹 Check DB connection
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
    except Exception:
        db_status = "Error"

    # 🔹 Check LLM config
    if not os.getenv("OPENROUTER_API_KEY"):
        llm_status = "Missing API Key"

    return templates.TemplateResponse("status.html", {
        "request": request,
        "backend": "OK",
        "database": db_status,
        "llm": llm_status
    })

@app.get("/run/{run_id}", response_class=HTMLResponse)
def view_run(run_id: int, request: Request):
    db: Session = SessionLocal()

    run = db.query(RunHistory).filter(RunHistory.id == run_id).first()

    if not run:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": "Run not found"
        })

    return templates.TemplateResponse("index.html", {
        "request": request,
        "outputs": json.loads(run.step_outputs),
        "previous_text": run.input_text,
        "runs": db.query(RunHistory).order_by(RunHistory.id.desc()).all()
    })
