
from fastapi import FastAPI
from pydantic import BaseModel

import requests

import Centroid

class Kakaomap(BaseModel):
    place_name: str
    axis_x: float
    axis_y: float
    address: str
    place_url: str
    place_ID: str


class Keyword():
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    headers = {"Authorization": "60f67244349d7ae054b6216815c8431a"}
    
class Coord2address():
    url = "https://dapi.kakao.com/v2/local/geo/coord2address.json"
    headers = {"Authorization": "60f67244349d7ae054b6216815c8431a"}
        
app = FastAPI()

# Data list for both front and back ends
@app.get("/maps/{place_name}")
async def request_coord2address(place_name: str):
    places = requests.get(Coord2address.url, headers=Coord2address.headers).json()['documents']
    return places

@app.get("/maps/{place_name}")
async def request_keyword(place_name: str):
    places = requests.get(Keyword.url, headers=Keyword.headers, y=Centroid.axis_y, x=Centroid.axis_x, 
                          radius=2000, category_group_code='SW8').json()['documents']
    return places


