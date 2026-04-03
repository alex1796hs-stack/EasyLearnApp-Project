from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class LessonContent(Base):
    __tablename__ = "lesson_contents"

    id = Column(Integer, primary_key=True, index=True)

    lesson_id = Column(Integer, ForeignKey("lessons.id"))

    title = Column(String, nullable=False)
    explanation = Column(String, nullable=False)