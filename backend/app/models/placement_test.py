from sqlalchemy import Column, Integer, Boolean, JSON, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class PlacementTest(Base):
    __tablename__ = "placement_tests"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    questions = Column(JSON)
    user_answers = Column(JSON, nullable=True)

    score = Column(Integer, default=0)

    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())

    user = relationship("User")