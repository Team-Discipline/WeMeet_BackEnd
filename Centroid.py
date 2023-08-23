# Calculate centroid
from fastapi import FastAPI
from pydantic import BaseModel

from Query import Kakaomap

import numpy as np

temp_x = []
temp_y = []


    
app = FastAPI()

"""
@app.get("/maps/{place_name}")
def append_axis(place_name: str):
    temp_x.append(Kakaomap.axis_x)
    temp_y.append(Kakaomap.axis_y)
"""

@app.post("/maps/{place_name}/centre")
async def calc_centroid(place_name: str):
    axis_x = np.mean(temp_x)
    axis_y = np.mean(temp_y)
    return {"axis_x": Centrepoint.axis_x,
            "axis_y": Centrepoint.axis_y}
    
