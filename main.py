import json
from pathlib import Path
from fastapi import FastAPI, HTTPException
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address, default_limits=["1/1second"])
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)


BASE_DIR = Path(__file__).resolve().parent
LEVELS_FILE = BASE_DIR / "levels.json"

try:
    with LEVELS_FILE.open("r", encoding="utf-8") as file:
        database = json.load(file)
except Exception as e:
    print(f"Failed to load levels.json: {e}")
    database = {}
@app.get("/")
def levellist():
    return list(database.keys())


@app.get("/level/{level}")
def findlevel(level: str):
    if level not in database:
        raise HTTPException(status_code=404, detail="Level not found")
    else:
        return database[level]
