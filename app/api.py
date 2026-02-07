from fastapi import FastAPI
from app.daily_runner import run_daily_pipeline

app = FastAPI(title="CurateAI API")

@app.get("/")
def root():
    return {"status": "CurateAI is running"}

@app.post("/run")
def run_pipeline():
    run_daily_pipeline()
    return {"status": "Pipeline executed successfully"}
