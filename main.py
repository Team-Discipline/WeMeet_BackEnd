from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from Query import Kakaomap
from answer import answer_router
from question import question_router


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
async def get_point(place_name: str):
    return {"place_name": Kakaomap.place_name,
            "axis_x": Kakaomap.axis_x,
            "axis_y": Kakaomap.axis_y,
            "address": Kakaomap.address,
            "place_url": Kakaomap.place_url,
            "place_ID": Kakaomap.place_ID}
