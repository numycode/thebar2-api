import json
from pathlib import Path

from fastapi import FastAPI, HTTPException

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
LEVELS_FILE = BASE_DIR / "levels.json"

with LEVELS_FILE.open("r", encoding="utf-8") as file:
    database = json.load(file)
@app.get("/")
def levellist():
    return list(database.keys())


@app.get("/level/{level}")
def findlevel(level: str):
    if level not in database:
        raise HTTPException(status_code=404, detail="Level not found")
    else:
        return database[level]
