
from typing import List

from fastapi import APIRouter

from api.dtos.tweet import TweetWeatherRequest, TweetWeatherResponse
from api.application.tweet import TweetWeather

router = APIRouter()


@router.post("/weather/")
async def tweet_weather(request: TweetWeatherRequest) -> TweetWeatherResponse:
    entity = await TweetWeather(request).execute()

    return TweetWeatherResponse.model_validate(entity)
