import json
import sys
from pathlib import Path

from fastapi import FastAPI, HTTPException

app = FastAPI()
with open("levels.json", 'r+') as file:
    database = json.load(file)

l = Path("levels.json")
if l.exists():
    print("Database exists")
else:
    print("ERROR: Database doesn't exist!")


@app.get("/")
def levellist():
    return list(database.keys())


@app.get("/level/{level}")
def findlevel(level: str):
    if level not in database:
        raise HTTPException(status_code=404, detail="Level not found")
    else:
        return database[level]
