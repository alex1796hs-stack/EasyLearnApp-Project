from app.models.lesson_content import LessonContent
from app.models.lesson import Lesson
from app.database import SessionLocal

def seed_content():
    db = SessionLocal()

    # Create Unit 1: Present Time
    lesson = db.query(Lesson).filter(Lesson.id == 1).first()
    if lesson:
        db.delete(lesson)
        db.commit()

    lesson = Lesson(
        id=1, 
        title="Unit 1: Grammar - Present Time", 
        topic="present time", 
        level="C1"
    )
    db.add(lesson)
    db.commit()
    db.refresh(lesson)
    
    # Remove old content just in case
    db.query(LessonContent).filter(LessonContent.lesson_id == 1).delete()
    db.commit()

    contents = [
        LessonContent(
            lesson_id=1,
            title="1. Present Simple",
            explanation="""
We use the present simple for:
• General truths and facts (e.g., Water boils at 100 degrees).
• Current habits and routines, often with frequency adverbs (e.g., He always goes to work by train).
• Permanent situations and states (e.g., I live in London).
• Timetables and scheduled events in the future (e.g., The train leaves at 5 PM).
• Reviews, sports commentaries and dramatic narratives.
"""
        ),
        LessonContent(
            lesson_id=1,
            title="2. Present Continuous",
            explanation="""
We use the present continuous for:
• Actions happening right now (e.g., She is studying at the moment).
• Temporary situations (e.g., I'm living with my parents until I find a flat).
• Changing and developing situations (e.g., The climate is getting warmer).
• Annoying habits (with 'always', 'constantly') (e.g., You are always forgetting your keys!).
• Definite future arrangements (e.g., We are meeting John tonight).
"""
        ),
        LessonContent(
            lesson_id=1,
            title="3. Present Perfect Simple",
            explanation="""
We use the present perfect simple for:
• Actions that happened at an unspecified time in the past (e.g., I have been to Paris).
• Actions that started in the past and continue to the present (e.g., I have known him for years).
• Actions that happened in the past but have a visible result in the present (e.g., She has broken her leg, so she can't walk).
• Experiences up to now, often with 'ever' or 'never'.
"""
        ),
        LessonContent(
            lesson_id=1,
            title="4. Present Perfect Continuous",
            explanation="""
We use the present perfect continuous for:
• Actions that started in the past and are still in progress, emphasizing the duration (e.g., I have been studying all day).
• Actions that have recently stopped, and their result is still visible (e.g., You look tired. Have you been running?).
• Note: We cannot use continuous tenses with stative verbs (know, like, believe, etc.).
"""
        ),
        LessonContent(
            lesson_id=1,
            title="5. Stative Verbs",
            explanation="""
Stative verbs describe states, not actions, and are not typically used in continuous tenses.
Examples: 
• Thoughts/Mental states: believe, know, understand, think (meaning 'have an opinion').
• Senses: hear, see, smell, taste, feel.
• Emotions/Feelings: love, hate, like, prefer.
• Possession: have, own, belong.

Note: Some verbs can be both stative and dynamic but with different meanings.
- I think it's a good idea. (State/Opinion)
- I am thinking about my holiday. (Action/Mental process)
"""
        )
    ]

    db.add_all(contents)
    db.commit()
    db.close()
    
    print("Lesson Content Seeded!")

if __name__ == "__main__":
    seed_content()