import json
from app.database import SessionLocal
from app.models.lesson import Lesson
from app.models.lesson_content import LessonContent

def generate_content(topic):
    # -----------------------
    # GRAMMAR: Present Time
    # -----------------------
    if topic == "present time":
        return [
            {
                "type": "intro",
                "order": 1,
                "title": "1. Present Simple",
                "explanation": "We use the present simple for: General truths, habits, routines, and permanent situations."
            },
            {
                "type": "concept",
                "order": 2,
                "title": "2. Present Continuous",
                "explanation": "We use the present continuous for: Actions happening now, temporary situations, and changing situations."
            },
            {
                "type": "concept",
                "order": 3,
                "title": "3. Present Perfect Simple",
                "explanation": "We use the present perfect simple for actions that happened at an unspecified time in the past or continue to the present."
            },
            {
                "type": "concept",
                "order": 4,
                "title": "4. Present Perfect Continuous",
                "explanation": "We use the present perfect continuous for actions that started in the past and are still in progress, emphasizing duration."
            },
            {
                "type": "advanced",
                "order": 5,
                "title": "5. Stative Verbs",
                "explanation": "Stative verbs (know, like, belong) describe states and are not typically used in continuous tenses."
            }
        ]

    # -----------------------
    # GRAMMAR: Past Time
    # -----------------------
    if topic == "past time":
        return [
            {
                "type": "intro",
                "order": 1,
                "title": "Understanding Past Time",
                "explanation": "Past time forms are used to describe actions that happened before now."
            },
            {
                "type": "concept",
                "order": 2,
                "title": "Past Simple",
                "explanation": "Used for completed actions.\n\nExample: She finished her homework."
            },
            {
                "type": "concept",
                "order": 3,
                "title": "Past Continuous",
                "explanation": "Used for actions in progress.\n\nExample: I was studying when he called."
            },
            {
                "type": "concept",
                "order": 4,
                "title": "Past Perfect",
                "explanation": "Used for actions before another past action.\n\nExample: She had left before I arrived."
            },
            {
                "type": "comparison",
                "order": 5,
                "title": "Past Simple vs Continuous",
                "explanation": "Simple = finished, Continuous = in progress."
            },
            {
                "type": "advanced",
                "order": 6,
                "title": "Past Perfect Continuous",
                "explanation": "Used for duration before another past action."
            }
        ]

    # -----------------------
    # VOCABULARY: Thinking & Learning
    # -----------------------
    if topic == "thinking and learning":
        return [
            {
                "type": "vocabulary",
                "order": 1,
                "title": "Topic Vocabulary",
                "explanation": "acquire knowledge, retain information, cognitive skills"
            },
            {
                "type": "vocabulary",
                "order": 2,
                "title": "Phrasal Verbs",
                "explanation": "figure out, pick up, take in"
            },
            {
                "type": "vocabulary",
                "order": 3,
                "title": "Collocations",
                "explanation": "make progress, do research, gain experience"
            },
            {
                "type": "vocabulary",
                "order": 4,
                "title": "Idioms",
                "explanation": "learn by heart, a quick learner"
            },
            {
                "type": "vocabulary",
                "order": 5,
                "title": "Word Formation",
                "explanation": "learn → learner → learning"
            }
        ]

    # -----------------------
    # DEFAULT (para el resto)
    # -----------------------
    return [
        {
            "type": "intro",
            "order": 1,
            "title": topic.title(),
            "explanation": f"This lesson introduces the topic of {topic}."
        },
        {
            "type": "concept",
            "order": 2,
            "title": "Core Concepts",
            "explanation": f"In this lesson, you will learn the key ideas related to {topic}."
        }
    ]

def run_seed():
    db = SessionLocal()

    # 1. Limpiar datos previos para evitar IDs duplicados
    try:
        db.query(LessonContent).delete()
        db.query(Lesson).delete()
        db.commit()
        print("✔ Database cleared for fresh seeding.")
    except Exception as e:
        db.rollback()
        print(f"✘ Error clearing database: {e}")

    # 2. Cargar JSON
    try:
        with open("data/curriculum.json", "r", encoding="utf-8") as f:
            curriculum = json.load(f)
    except FileNotFoundError:
        print("✘ Error: curriculum.json not found in data folder.")
        return

    # 3. Loop principal
    for unit in curriculum:
        lesson_level = "C1"
        
        # Crear lección
        lesson = Lesson(
            title=unit["title"],
            topic=unit["topic"],
            level=lesson_level,
            order=unit["unit"]
        )

        db.add(lesson)
        db.flush()

        # Generar contenido
        content_blocks = generate_content(unit["topic"])

        for block in content_blocks:
            content = LessonContent(
                lesson_id=lesson.id,
                type=block["type"],
                order=block["order"],
                title=block["title"],
                explanation=block["explanation"]
            )
            db.add(content)

    db.commit()
    db.close()
    print(f"✅ Successfully seeded {len(curriculum)} units and their content.")

if __name__ == "__main__":
    run_seed()