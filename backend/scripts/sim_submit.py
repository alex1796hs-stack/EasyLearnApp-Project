from app.database import SessionLocal
from app.models.placement_test import PlacementTest
from app.routes.placement import submit_test
from app.schemas.placement import PlacementSubmit, PlacementAnswer

db = SessionLocal()
test = db.query(PlacementTest).order_by(PlacementTest.id.desc()).first()

if not test:
    print("No test found")
else:
    # Get the correct answer for the first question
    q1 = test.questions[0]
    q1_id = q1["id"]
    correct_ans = q1["correct"]

    # create a mock current_user
    from app.models.user import User
    user = db.query(User).filter_by(id=test.user_id).first()
    
    # ensure it's not completed so we can test
    test.completed = False
    db.commit()

    ans = PlacementAnswer(question_id=q1_id, answer=correct_ans)
    submit = PlacementSubmit(answers=[ans])
    
    # Simulate internal logic
    if isinstance(test.questions, str):
        import json
        qs = json.loads(test.questions)
    else:
        qs = test.questions
        
    print("q1_id type:", type(q1_id), "val:", q1_id)
    print("qs[0] id type:", type(qs[0]["id"]), "val:", qs[0]["id"])
    
    res = submit_test(answers=submit, current_user=user, db=db)
    print("Result:", res)

db.close()
