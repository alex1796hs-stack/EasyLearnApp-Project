from app.models.lesson_content import LessonContent
from app.models.lesson import Lesson
from app.database import SessionLocal

db = SessionLocal()

# Ensure at least one lesson exists before adding content to it
lesson = db.query(Lesson).filter(Lesson.id == 1).first()
if not lesson:
    lesson = Lesson(id=1, title="Basic English Grammar", content="Fundamentals of grammar.", level="A2")
    db.add(lesson)
    db.commit()
    db.refresh(lesson)

contents = [
    LessonContent(
        lesson_id=1,
        title="Present Simple",
        explanation="""
We use the present simple for habits and routines.

Examples:
- I go to the gym every day
- She works in London
"""
    ),
    LessonContent(
        lesson_id=1,
        title="Present Continuous",
        explanation="""
We use the present continuous for actions happening now.

Examples:
- I am studying right now
- She is working at the moment
"""
    )
]

db.add_all(contents)
db.commit()
db.close()