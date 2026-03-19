from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.lesson import Lesson
from app.database import SessionLocal
from app.models.user import User
from app.models.placement_test import PlacementTest
from app.models.progress import Progress
from app.core.security import get_current_user

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
def get_dashboard(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    placement = db.query(PlacementTest).filter(
        PlacementTest.user_id == current_user.id,
        PlacementTest.completed == True
    ).order_by(PlacementTest.id.desc()).first()

    completed_lessons = db.query(Progress).filter(
        Progress.user_id == current_user.id
    ).count()

    total_lessons = db.query(Lesson).count()
    progress_percentage = round((completed_lessons / total_lessons * 100), 2) if total_lessons > 0 else 0

    return {
    "level": current_user.level,
    "placement_score": placement.score if placement else 0,
    "completed_lessons": completed_lessons,
    "total_lessons": total_lessons,
    "progress_percentage": progress_percentage
}