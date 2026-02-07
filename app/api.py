from fastapi import FastAPI
from app.daily_runner import run_daily_pipeline

app = FastAPI(title="AI News Aggregator")

@app.get("/")
def root():
    return {"status": "AI News Aggregator is running"}

@app.get("/run")
def run_pipeline():
    run_daily_pipeline()
    return {"status": "Pipeline executed successfully"}
