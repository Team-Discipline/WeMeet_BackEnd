from datetime import datetime

from pydantic import BaseModel, validator

from WeMeet_BackEnd.DB.models import Answer


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answer: list[Answer] = []

    class Config:
        orm_mode = True


class QuestionCreate(BaseModel):
    subject: str
    content: str

    @validator('subject', 'content')
    def not_empty(self, value):
        if not value or not value.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return value


class QuestionList(BaseModel):
    total: int = 0
    question_list: list[Question] = []
