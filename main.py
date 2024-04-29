from fastapi import FastAPI
from dotenv import load_dotenv

from routers import tweet

load_dotenv("api/.env")

app = FastAPI()

@app.get("/")
@app.get("/healthcheck")
async def healthcheck():
    return True

app.include_router(tweet.router, prefix="/tweet", tags=["tweet"])
