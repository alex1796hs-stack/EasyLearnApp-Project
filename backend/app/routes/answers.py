from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.models.user_answer import UserAnswer
from app.schemas.answer import AnswerCreate
from app.core.security import get_current_user

router = APIRouter(tags=["Answers"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/answers")
def save_answer(
    answer: AnswerCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_answer = UserAnswer(
        user_id=current_user.id,
        question_id=answer.question_id,
        is_correct=answer.is_correct
    )

    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)

    return {"message": "Answer saved"}
