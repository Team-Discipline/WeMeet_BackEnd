from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

import requestmap
from DB import models, schemas, crud
from DB.database import SessionLocal, engine, get_db
from answer import answer_router
from question import question_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(requestmap.router)

# CORS 설정
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def hello():
    return {"message": "hello"}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="이미 등록된 이메일입니다.")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="등록된 정보가 없습니다.")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
        user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.post("/maps/{place_name}/stored", response_model=schemas.Place)
def create_place(place: schemas.PlaceCreate, db: Session = Depends(get_db)):
    db_place = crud.get_place(db, place_ID=place.place_ID)
    if db_place:
        raise HTTPException(status_code=400, detail="등록된 장소입니다.")
    return crud.create_place(db=db, place=place)


@app.get("/maps/{place_name}/stored", response_model=schemas.Place)
def read_place(place_ID: int, db: Session = Depends(get_db)):
    db_place = crud.get_place(db, place_ID=place_ID)
    if db_place is None:
        raise HTTPException(status_code=404, detail="장소를 찾을 수 없습니다.")
    return db_place
