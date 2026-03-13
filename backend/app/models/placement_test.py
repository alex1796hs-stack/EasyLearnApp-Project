from sqlalchemy import Column, Integer, Boolean, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class PlacementTest(Base):
    __tablename__ = "placement_tests"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    questions = Column(JSON)

    score = Column(Integer, default=0)

    completed = Column(Boolean, default=False)

    user = relationship("User")