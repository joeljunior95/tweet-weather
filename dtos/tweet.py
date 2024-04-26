from pydantic import BaseModel, ConfigDict, EmailStr, Field, HttpUrl


class TweetWeatherRequest(BaseModel):
    location: str = Field(min_length=3)

class TweetWeatherResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    content: str
