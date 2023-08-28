from datetime import datetime

from pydantic import BaseModel, validator

from answer.answer_schema import Answer


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime
    answers: list[Answer] = []

    class Config:
        from_attributes = True


class QuestionCreate(Question):
    subject: str
    content: str

    @validator('subject')
    def not_empty_subject(cls, value):
        if not value or not value.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return value

    @validator('content')
    def not_empty_content(cls, value):
        if not value or not value.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return value


class QuestionList(BaseModel):
    total: int = 0
    question_list: list[Question] = []
