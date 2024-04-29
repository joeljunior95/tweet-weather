from pydantic import BaseModel, ConfigDict, EmailStr, Field, HttpUrl


class TweetWeatherRequest(BaseModel):
    city: str = Field(min_length=3)
    state: str = Field(min_length=2)
    country: str = Field(min_length=2)

class TweetWeatherResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    content: str
