from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import requests

REST_API_KEY = "60f67244349d7ae054b6216815c8431a"

router = APIRouter(
    prefix="/requestMap",
)

# FE에서 사용자가 입력한 주소들을 query에 콤마로 구분하여 입력
# 주소 입력 예시는 다음과 같음: 서울 강남구 삼성동 159,서울 강남구 영동대로 513
# Kakao API에 주소를 요청. 두 주소의 y,x값 평균을 구하여 average_y, average_x로 반환
# 그 후 average_y, average_x의 반경 1.5km 이내의 지하철 역을 검색후 json 형식으로 반환함

"""
요청 후 return은 json 형식으로 아래와 같음
------------------------------------------

{
  "documents": [
    {
      "address_name": "서울 강남구 삼성동 172",
      "category_group_code": "SW8",
      "category_group_name": "지하철역",
      "category_name": "교통,수송 > 지하철,전철 > 수도권9호선",
      "distance": "256",
      "id": "26550131",
      "phone": "02-2656-0929",
      "place_name": "봉은사역 9호선",
      "place_url": "http://place.map.kakao.com/26550131",
      "road_address_name": "서울 강남구 봉은사로 지하 601",
      "x": "127.060233935114",
      "y": "37.5142554489848"
    },
    {
      "address_name": "서울 강남구 삼성동 172-66",
      "category_group_code": "SW8",
      "category_group_name": "지하철역",
      "category_name": "교통,수송 > 지하철,전철 > 수도권2호선",
      "distance": "515",
      "id": "21160620",
      "phone": "02-6110-2191",
      "place_name": "삼성역 2호선",
      "place_url": "http://place.map.kakao.com/21160620",
      "road_address_name": "서울 강남구 테헤란로 지하 538",
      "x": "127.06302321147605",
      "y": "37.508822740225305"
    },
    {
      "address_name": "서울 강남구 삼성동 111-147",
      "category_group_code": "SW8",
      "category_group_name": "지하철역",
      "category_name": "교통,수송 > 지하철,전철 > 수도권9호선",
      "distance": "532",
      "id": "26550128",
      "phone": "02-2656-0928",
      "place_name": "삼성중앙역 9호선",
      "place_url": "http://place.map.kakao.com/26550128",
      "road_address_name": "서울 강남구 봉은사로 지하 501",
      "x": "127.053043676912",
      "y": "37.5129614511319"
    },
    {
      "address_name": "서울 강남구 청담동 77-76",
      "category_group_code": "SW8",
      "category_group_name": "지하철역",
      "category_name": "교통,수송 > 지하철,전철 > 수도권7호선",
      "distance": "932",
      "id": "21161041",
      "phone": "02-6311-7291",
      "place_name": "청담역 7호선",
      "place_url": "http://place.map.kakao.com/21161041",
      "road_address_name": "서울 강남구 학동로 지하 508",
      "x": "127.053717937903",
      "y": "37.519455579961"
    },
    {
      "address_name": "서울 강남구 삼성동 172-66",
      "category_group_code": "SW8",
      "category_group_name": "지하철역",
      "category_name": "교통,수송 > 지하철,전철 > 수도권2호선",
      "distance": "1229",
      "id": "21160804",
      "phone": "02-6110-2201",
      "place_name": "선릉역 2호선",
      "place_url": "http://place.map.kakao.com/21160804",
      "road_address_name": "서울 강남구 테헤란로 지하 340",
      "x": "127.04896282498558",
      "y": "37.504497373023206"
    },
    {
      "address_name": "서울 송파구 잠실동 122",
      "category_group_code": "SW8",
      "category_group_name": "지하철역",
      "category_name": "교통,수송 > 지하철,전철 > 수도권2호선",
      "distance": "1318",
      "id": "21160812",
      "phone": "02-6110-2181",
      "place_name": "종합운동장역 2호선",
      "place_url": "http://place.map.kakao.com/21160812",
      "road_address_name": "서울 송파구 올림픽로 지하 23",
      "x": "127.073849447402",
      "y": "37.5111446632705"
    },
    {
      "address_name": "서울 강남구 삼성동 111-114",
      "category_group_code": "SW8",
      "category_group_name": "지하철역",
      "category_name": "교통,수송 > 지하철,전철 > 수인분당선",
      "distance": "1365",
      "id": "21160738",
      "phone": "02-511-4761",
      "place_name": "선정릉역 수인분당선",
      "place_url": "http://place.map.kakao.com/21160738",
      "road_address_name": "서울 강남구 선릉로 지하 580",
      "x": "127.043627289129",
      "y": "37.5109326388803"
    },
    {
      "address_name": "서울 강남구 삼성동 172-66",
      "category_group_code": "SW8",
      "category_group_name": "지하철역",
      "category_name": "교통,수송 > 지하철,전철 > 수인분당선",
      "distance": "1196",
      "id": "21161056",
      "phone": "1544-7788",
      "place_name": "선릉역 수인분당선",
      "place_url": "http://place.map.kakao.com/21161056",
      "road_address_name": "서울 강남구 테헤란로 지하 340",
      "x": "127.04870992465413",
      "y": "37.505167825521674"
    },
    {
      "address_name": "서울 강남구 삼성동 111-114",
      "category_group_code": "SW8",
      "category_group_name": "지하철역",
      "category_name": "교통,수송 > 지하철,전철 > 수도권9호선",
      "distance": "1339",
      "id": "26550129",
      "phone": "02-2656-0927",
      "place_name": "선정릉역 9호선",
      "place_url": "http://place.map.kakao.com/26550129",
      "road_address_name": "서울 강남구 선릉로 지하 580",
      "x": "127.0440148858615",
      "y": "37.51032431709664"
    }
  ],
  "meta": {
    "is_end": true,
    "pageable_count": 9,
    "same_name": {
      "keyword": "지하철역",
      "region": [],
      "selected_region": ""
    },
    "total_count": 68
  }
}



"""


# /average_coordinates/ 엔드포인트에서 한 번에 지하철 역 정보까지 처리함

@router.get("/average_coordinates/")
async def average_coordinates(queries: str):
    url = "https://dapi.kakao.com/v2/local/search/address.json"
    subway_url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    radius = 1500  # 반경 1.5km 이내

    headers = {
        "Authorization": f"KakaoAK {REST_API_KEY}"
    }

    query_list = queries.split(',')  # 여러 쿼리를 콤마로 구분하여 리스트로 변환

    total_y = 0
    total_x = 0
    count = 0

    for query in query_list:
        params = {
            "query": query
        }

        # 입력된 주소로 Kakao API에 요청
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            for document in data.get("documents", []):
                y = float(document.get("y", 0))
                x = float(document.get("x", 0))
                total_y += y
                total_x += x
                count += 1

    if count > 0:
        average_y = total_y / count
        average_x = total_x / count

        # 요청 후 계산된 average_y, average_x를 바탕으로 반경 1.5km 내의 지하철 역 요청
        subway_params = {
            "y": average_y,
            "x": average_x,
            "radius": radius,
            "query": "지하철역"
        }

        subway_response = requests.get(subway_url, headers=headers, params=subway_params)

        if subway_response.status_code == 200:
            subway_data = subway_response.json()
            if "documents" in subway_data and len(subway_data["documents"]) > 0:
                return subway_data
            else:
                return {"message": "No subway stations found"}
        else:
            return {"message": "Kakao API request failed for subway search"}
    else:
        return {"message": "No valid coordinates found"}
