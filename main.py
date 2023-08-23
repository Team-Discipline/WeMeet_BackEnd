from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from answer import answer_router
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
app.include_router(answer_router.router)


origins = [
    "http://localhost:3000",  # 프론트엔드 주소
    "http://127.0.0.1:3000",  # 프론트엔드 주소
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"message": "Hello, World"}


@app.get("/maps/{place_name}")
async def get_point(query):
    return {"place_name": Coordinate.place_name,
            "axis_x": Coordinate.axis_x,
            "axis_y": Coordinate.axis_y,
            "address": Coordinate.address,
            "place_url": Coordinate.place_url,
            "place_ID": Coordinate.place_ID}
