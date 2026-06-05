import json
import sys
from pathlib import Path

from fastapi import FastAPI, HTTPException

api = FastAPI()

l = Path("levels.json")
if l.exists():
    print("Database exists")
else:
    print("ERROR: Database doesn't exist!")
    sys.exit(255)
with open("levels.json", 'r+') as file:
    database = json.load(file)


@api.get("/")
def levellist():
    return list(database.keys())


@api.get("/level/{level}")
def findlevel(level: str):
    if level not in database:
        raise HTTPException(status_code=404, detail="Level not found")
    else:
        return database[level]
