from app.database import SessionLocal
from app.models.placement_test import PlacementTest
db = SessionLocal()
t = db.query(PlacementTest).order_by(PlacementTest.id.desc()).first()
if t and t.questions:
    print('First Question:', t.questions[0])
    print('Completed:', t.completed)
    print('Score:', t.score)
else:
    print('No questions or test')
db.close()
