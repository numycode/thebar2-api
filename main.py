import json

from fastapi import FastAPI, HTTPException

app = FastAPI()
with open("levels.json", 'r+') as file:
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
