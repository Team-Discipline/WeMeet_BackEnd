from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from DB.database import get_db, SessionLocal
from DB.models import Question
from question import question_schema, question_crud

router = APIRouter(
    prefix="/question",
)


@router.get("/list", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    # db = SessionLocal()
    # _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    # db.close()
    # _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    _question_list = question_crud.get_question_list(db)
    return _question_list


@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    return question


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.QuestionCreate,
                    db: Session = Depends(get_db)):
    question_crud.create_question(db=db, question_create=_question_create)
