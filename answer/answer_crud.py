from datetime import datetime

from sqlalchemy.orm import Session

from DB.models import Question, Answer
from answer.answer_schema import AnswerCreate


def create_answer(db: Session, question: Question, answer_create: AnswerCreate):
    db_answer = Answer(question=question,
                       content=answer_create.content,
                       create_date=datetime.now())
    db.add(db_answer)
    db.commit()


