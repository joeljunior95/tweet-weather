from dataclasses import dataclass
from datetime import datetime
from os import getenv
from typing import Iterable
import tweepy
from pydantic import BaseModel

from dtos.tweet import TweetWeatherRequest
from entities import BaseEntity
from entities.tweet import TweetWeatherEntity
from application import BaseApplication
from vendor.owmpy import OpenWeatherMap


class TweetWeather(BaseApplication):
    request: TweetWeatherRequest

    def __init__(self, request: TweetWeatherRequest):
        self.request = request
        self.api_key = getenv("OPEN_WEATHER_MAP_API_KEY")
        self.consumer_key = getenv("TWITTER_CONSUMER_KEY")
        self.consumer_secret = getenv("TWITTER_CONSUMER_SECRET")
        self.access_token = getenv("TWITTER_ACCESS_TOKEN")
        self.access_secret = getenv("TWITTER_ACCESS_TOKEN_SECRET")
        self.bearer_token = getenv("TWITTER_BEARER_TOKEN")

    async def execute(self) -> BaseEntity:
        weather = OpenWeatherMap(self.api_key, self.request.location)
        forecasts = weather.weather_info(None,days_forward=6)

        client = tweepy.Client(self.bearer_token,
                        self.consumer_key,
                        self.consumer_secret,
                        self.access_token,
                        self.access_secret)
 
        tweet = f"Previsão do tempo {weather.city}, {weather.state}: "
        for i in range(0,len(forecasts)):
            forecast = forecasts[i]
            tweet += f"em {datetime.strptime(forecast.date, '%Y-%m-%d').strftime('%d/%m')} MAX {int(forecast.temperature.max)}°C e MIN {int(forecast.temperature.min)}°C"
            if i == len(forecasts) - 2:
                tweet += " e "
            elif i == len(forecasts) - 1:
                tweet += "."
            else:
                tweet += ", "

        response = client.create_tweet(text=tweet)

        # TODO tratativa de erros e exceptions

        entity = TweetWeatherEntity(response.data["id"],
                                    response.data["text"],
                                    forecasts)


        return entity
