from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, Integer
from app.database import SessionLocal
from app.models.user import User
from app.models.user_answer import UserAnswer
from app.models.question_bank import QuestionBank
from app.core.security import get_current_user

router = APIRouter(tags=["Review"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/review/questions")
def get_review_questions(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Returns the questions the user has answered incorrectly most often.
    Only includes questions where the user has at least one incorrect answer,
    and where the total incorrect answers exceed the correct ones (net negative).
    """

    # Aggregate correct and incorrect counts per question for this user
    answers = (
        db.query(
            UserAnswer.question_id,
            func.count(UserAnswer.id).label("total"),
            func.sum(UserAnswer.is_correct.cast(Integer)).label("correct_count")
        )
        .filter(UserAnswer.user_id == current_user.id)
        .group_by(UserAnswer.question_id)
        .all()
    )

    # Keep only questions where incorrect answers outnumber correct ones
    weak_question_ids = []
    for row in answers:
        correct = row.correct_count or 0
        incorrect = row.total - correct
        if incorrect > correct:
            weak_question_ids.append(row.question_id)

    if not weak_question_ids:
        return {"questions": [], "message": "no_weak_questions"}

    # Fetch the actual question data from the question bank
    questions = (
        db.query(QuestionBank)
        .filter(QuestionBank.id.in_(weak_question_ids))
        .limit(15)  # Cap at 15 questions per review session
        .all()
    )

    return {
        "questions": [
            {
                "id": q.id,
                "question": q.question,
                "options": q.options,
                "correct": q.correct,
                "topic": q.topic,
                "difficulty": q.difficulty,
            }
            for q in questions
        ],
        "message": "ok"
    }
