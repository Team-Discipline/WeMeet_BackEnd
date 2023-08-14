from fastapi import FastAPI
from pydantic import BaseModel

from question import question_router


class Coordinate(BaseModel):
    place_name: str
    axis_x: float
    axis_y: float
    address: str
    place_url: str
    place_ID: str


app = FastAPI()
app.include_router(question_router.router)


@app.get("/maps/{place_name}")
async def get_point(query):
    return {"place_name": Coordinate.place_name,
            "axis_x": Coordinate.axis_x,
            "axis_y": Coordinate.axis_y,
            "address": Coordinate.address,
            "place_url": Coordinate.place_url,
            "place_ID": Coordinate.place_ID}
