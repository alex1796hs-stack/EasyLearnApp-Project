from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.lesson import Lesson
from app.schemas.lesson import LessonCreate, LessonResponse
from app.models.progress import Progress
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(prefix="/lessons", tags=["Lessons"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=LessonResponse)
def create_lesson(lesson: LessonCreate, db: Session = Depends(get_db)):
    new_lesson = Lesson(**lesson.dict())
    db.add(new_lesson)
    db.commit()
    db.refresh(new_lesson)
    return new_lesson


@router.get("/", response_model=list[LessonResponse])
def list_lessons(db: Session = Depends(get_db)):
    return db.query(Lesson).all()

@router.get("/next")
def get_next_lesson(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    completed_lessons = db.query(Progress.lesson_id).filter(
        Progress.user_id == current_user.id
    )

    next_lesson = db.query(Lesson).filter(
        ~Lesson.id.in_(completed_lessons)
    ).order_by(Lesson.id).first()

    if not next_lesson:
        raise HTTPException(
            status_code=404,
            detail="No more lessons available"
        )
        
    from app.models.lesson_content import LessonContent
    contents = db.query(LessonContent).filter(LessonContent.lesson_id == next_lesson.id).all()
    
    lesson_dict = next_lesson.__dict__.copy()
    lesson_dict.pop("_sa_instance_state", None)
    
    lesson_dict["content"] = [
        {"title": c.title, "explanation": c.explanation} for c in contents
    ]

    from app.services.question_service import get_questions_by_level
    practice_questions = get_questions_by_level(db, next_lesson.level, 3)

    lesson_dict["questions"] = [
        {
            "id": q.id,
            "question": q.question,
            "options": q.options,
            "correct": q.correct
        } for q in practice_questions
    ]

    return lesson_dict