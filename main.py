import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


from answer import answer_router
from question import question_router
from subway_station import subwayStation_router


class Coordinate(BaseModel):
    place_name: str
    axis_x: float
    axis_y: float
    address: str
    place_url: str
    place_ID: str


app = FastAPI()
app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(subwayStation_router.router)


@app.get("/maps/{place_name}")
async def get_point(query):
    return {"place_name": Coordinate.place_name,
            "axis_x": Coordinate.axis_x,
            "axis_y": Coordinate.axis_y,
            "address": Coordinate.address,
            "place_url": Coordinate.place_url,
            "place_ID": Coordinate.place_ID}


if __name__ == '__main__':
    uvicorn.run(app, host = "0.0.0.0", port = 8000)