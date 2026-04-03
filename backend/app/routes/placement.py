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

    questions_db += get_questions_by_level(db, "A2", 6)
    questions_db += get_questions_by_level(db, "B1", 6)
    questions_db += get_questions_by_level(db, "B2", 6)
    questions_db += get_questions_by_level(db, "C1", 6)
    questions_db += get_questions_by_level(db, "C2", 6)

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
            "correct": q.correct,
            "difficulty": q.difficulty
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

    summary = []
    for ans in answers.answers:
        question = next(
            (q for q in questions if q["id"] == ans.question_id),
            None
        )

        if not question:
            continue

        is_correct = ans.answer == question["correct"]
        if is_correct:
            difficulty = question.get("difficulty", "A2")
            score += level_weights.get(difficulty, 1)
        
        summary.append({
            "question": question["question"],
            "user_answer": ans.answer,
            "correct_answer": question["correct"],
            "is_correct": is_correct
        })

    # CEFR scale (weighted) - 27 questions model (max score 87)
    if score <= 17:
        level = "A2"
    elif score <= 34:
        level = "B1"
    elif score <= 52:
        level = "B2"
    elif score <= 70:
        level = "C1"
    else:
        level = "C2"

    # Re-obtener el usuario para que esté en la misma sesión 'db'
    db_user = db.query(User).filter(User.id == current_user.id).first()
    db_user.level = level
    
    test.score = score
    test.completed = True
    
    db.commit()

    return {
        "score": score,
        "level": level,
        "summary": summary
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
        "level": test.user.level,
        "score": test.score,
        "total_questions": total_questions
    }