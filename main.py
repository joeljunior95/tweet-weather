from fastapi import FastAPI
from dotenv import load_dotenv

from routers import tweet

load_dotenv("api/.env")

app = FastAPI()

app.include_router(tweet.router, prefix="/tweet", tags=["tweet"])
