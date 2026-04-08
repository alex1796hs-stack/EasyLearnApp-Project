from pydantic import BaseModel


class LessonCreate(BaseModel):
    title: str
    topic: str
    level: str


class LessonResponse(BaseModel):
    id: int
    title: str
    topic: str
    level: str

    class Config:
        from_attributes = True