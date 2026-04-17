from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import SessionLocal
from app.models.user import User
from app.models.lesson import Lesson
from app.models.placement_test import PlacementTest
from app.models.progress import Progress
from app.models.user_answer import UserAnswer
from app.core.security import get_current_user

router = APIRouter(prefix="/profile", tags=["Profile"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
def get_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Placement info
    placement = db.query(PlacementTest).filter(
        PlacementTest.user_id == current_user.id,
        PlacementTest.completed == True
    ).order_by(PlacementTest.id.desc()).first()

    # Progress stats
    completed_lessons = db.query(Progress).filter(
        Progress.user_id == current_user.id
    ).count()
    total_lessons = db.query(Lesson).count()
    progress_pct = round((completed_lessons / total_lessons * 100), 1) if total_lessons > 0 else 0

    # Answer stats
    total_answers = db.query(UserAnswer).filter(
        UserAnswer.user_id == current_user.id
    ).count()
    correct_answers = db.query(UserAnswer).filter(
        UserAnswer.user_id == current_user.id,
        UserAnswer.is_correct == True
    ).count()
    accuracy = round((correct_answers / total_answers * 100), 1) if total_answers > 0 else 0

    return {
        "email": current_user.email,
        "level": current_user.level,
        "placement_score": placement.score if placement else None,
        "completed_lessons": completed_lessons,
        "total_lessons": total_lessons,
        "progress_percentage": progress_pct,
        "total_answers": total_answers,
        "correct_answers": correct_answers,
        "accuracy": accuracy,
    }
