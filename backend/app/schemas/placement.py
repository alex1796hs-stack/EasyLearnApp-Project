from pydantic import BaseModel
from typing import List


class PlacementAnswer(BaseModel):
    question_id: int
    answer: str


class PlacementSubmit(BaseModel):
    answers: List[PlacementAnswer]