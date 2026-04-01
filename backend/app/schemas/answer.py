from pydantic import BaseModel


class AnswerCreate(BaseModel):
    question_id: int
    is_correct: bool
