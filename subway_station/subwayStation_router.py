from fastapi import FastAPI, HTTPException, APIRouter, Query
from typing import List

from subway_station.subwayStation_schema import Coordinate, SubwayStation

router = APIRouter(
    prefix="/subwayStation",
)

# 가상의 지하철 역 데이터
subway_stations = [
    {"name": "역1", "latitude": 37.12345, "longitude": 127.67890},
    {"name": "역2", "latitude": 37.23456, "longitude": 127.78901},
    {"name": "A", "latitude": 67.23456, "longitude": 327.78901},
    {"name": "B", "latitude": 77.23456, "longitude": 527.78901},
    {"name": "C", "latitude": 1237.23456, "longitude": 227.78901},
    {"name": "D", "latitude": 1257.23456, "longitude": 327.78901},

]


# 좌표와 거리 계산 함수
def calculate_distance(lat1, lon1, lat2, lon2):
    # 실제 거리 계산 로직 적용
    return abs(lat1 - lat2) + abs(lon1 - lon2)


@router.get("/find_subway_stations/")
async def find_subway_stations(latitude: float = Query(...), longitude: float = Query(...)):
    result = []

    for station in subway_stations:
        distance = calculate_distance(latitude, longitude, station["latitude"], station["longitude"])
        result.append(SubwayStation(name=station["name"], distance=distance))

    result.sort(key=lambda x: x.distance)
    return result