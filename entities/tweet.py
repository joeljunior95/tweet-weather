# from pydantic.dataclasses import dataclass
from dataclasses import dataclass
from typing import Optional, TypedDict, List

from entities import BaseEntity
from vendor.owmpy.models import DaySummary


class TweetWeather(TypedDict):
    id: Optional[str]
    content: str
    forecasts: List[DaySummary]


@dataclass
class TweetWeatherEntity(BaseEntity):
    id: Optional[str]
    content: str
    forecasts: List[DaySummary]

    @classmethod
    def from_dict(cls, other: dict):
        return cls(
            id=other.get("id"),
            content=other["content"],
            forecasts=other["forecasts"]
        )

    def to_dict(self) -> TweetWeather:
        return {
            "id": self.id,
            "content": self.content,
            "forecasts": self.forecasts
        }
