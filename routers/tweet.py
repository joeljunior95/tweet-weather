
from fastapi import APIRouter, HTTPException

from dtos.tweet import TweetWeatherRequest, TweetWeatherResponse
from application.tweet import TweetWeather, OWMException
from errors.tweet import TweetException

router = APIRouter()


@router.post("/weather/")
async def tweet_weather(request: TweetWeatherRequest) -> TweetWeatherResponse:
    try:
        entity = await TweetWeather(request).execute()

        return TweetWeatherResponse.model_validate(entity)
    except TweetException as ex:
        raise HTTPException(status_code=ex.http_code, detail=str(ex))