from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import random
import json
from app.database import SessionLocal
from app.services.question_service import get_questions_by_level
from app.models.placement_test import PlacementTest
from app.models.user import User
from app.core.security import get_current_user
from app.schemas.placement import PlacementSubmit
#from app.services.ai_service import generate_placement_test
router = APIRouter(prefix="/placement", tags=["Placement Test"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/start")
def start_test(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    questions_db = []

    questions_db += get_questions_by_level(db, "A2", 2)
    questions_db += get_questions_by_level(db, "B1", 2)
    questions_db += get_questions_by_level(db, "B2", 3)
    questions_db += get_questions_by_level(db, "C1", 2)
    questions_db += get_questions_by_level(db, "C2", 1)

    # remove duplicates
    unique_questions = {}

    for q in questions_db:
        unique_questions[q.id] = q

    questions_db = list(unique_questions.values())

    random.shuffle(questions_db)

    questions = [
        {
            "id": q.id,
            "question": q.question,
            "options": q.options,
            "correct": q.correct
        }
        for q in questions_db
    ]

    public_questions = [
        {
            "id": q["id"],
            "question": q["question"],
            "options": q["options"]
        }
        for q in questions
    ]

    test = PlacementTest(
        user_id=current_user.id,
        questions=questions
    )

    db.add(test)
    db.commit()

    return {
        "test_id": test.id,
        "questions": public_questions
    }

@router.post("/submit")
def submit_test(
    answers: PlacementSubmit,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    test = db.query(PlacementTest).filter(
        PlacementTest.user_id == current_user.id,
        PlacementTest.completed == False
    ).first()

    if not test:
        return {"error": "No test found"}

    score = 0

    level_weights = {
        "A2": 1,
        "B1": 2,
        "B2": 3,
        "C1": 4,
        "C2": 5
    }

    # load questions once
    if isinstance(test.questions, str):
        questions = json.loads(test.questions)
    else:
        questions = test.questions

    for ans in answers.answers:

        question = next(
            (q for q in questions if q["id"] == ans.question_id),
            None
        )

        if not question:
            continue

        if ans.answer == question["correct"]:
            difficulty = question.get("difficulty", "A2")
            score += level_weights.get(difficulty, 1)

    # CEFR scale (weighted)
    if score <= 8:
        level = "A2"
    elif score <= 14:
        level = "B1"
    elif score <= 20:
        level = "B2"
    elif score <= 26:
        level = "C1"
    else:
        level = "C2"

    current_user.level = level
    test.score = score
    test.completed = True

    db.commit()

    return {
        "score": score,
        "level": level
    }

@router.get("/result")
def get_placement_result(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    test = db.query(PlacementTest).filter(
        PlacementTest.user_id == current_user.id,
        PlacementTest.completed == True
    ).order_by(PlacementTest.id.desc()).first()

    if not test:
        return {"error": "No completed placement test found"}

    total_questions = len(test.questions)

    return {
        "level": current_user.level,
        "score": test.score,
        "total_questions": total_questions
    }