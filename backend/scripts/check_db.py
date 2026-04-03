from app.database import SessionLocal
from app.models.question_bank import QuestionBank

db = SessionLocal()
print('Total:', db.query(QuestionBank).count())
for level in ["A2", "B1", "B2", "C1", "C2"]:
    c = db.query(QuestionBank).filter(QuestionBank.difficulty == level).count()
    print(f"{level}: {c}")

db.close()
