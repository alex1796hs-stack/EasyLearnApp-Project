from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
from app.models.question_bank import QuestionBank


def get_random_questions(db: Session, limit: int = 30):
    return (
        db.query(QuestionBank)
        .order_by(func.random())
        .limit(limit)
        .all()
    )


def get_questions_by_level(db: Session, level: str, limit: int):
    return (
        db.query(QuestionBank)
        .filter(QuestionBank.difficulty == level)
        .order_by(func.random())
        .limit(limit)
        .all()
    )