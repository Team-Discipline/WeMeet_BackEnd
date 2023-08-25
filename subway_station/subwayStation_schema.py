from pydantic import BaseModel


class Coordinate(BaseModel):
    latitude: float
    longitude: float


class SubwayStation(BaseModel):
    name: str
    distance: float
