from sqlalchemy import Column, Integer, String, JSON
from app.database import Base

class QuestionBank(Base):

    __tablename__ = "question_bank"

    id = Column(Integer, primary_key=True, index=True)

    question = Column(String, nullable=False)

    options = Column(JSON, nullable=False)

    correct = Column(String, nullable=False)

    difficulty = Column(String)

    topic = Column(String)