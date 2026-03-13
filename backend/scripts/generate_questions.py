import random
from app.database import SessionLocal
from app.models.question_bank import QuestionBank

subjects = ["I", "She", "He", "They", "We"]
verbs = ["travel", "study", "work", "learn English", "improve"]

grammar_templates = [
    {
        "template": "If {s} ____ more time, {s_lower} would {v} more.",
        "options": ["has", "had", "have", "having"],
        "correct": "had",
        "difficulty": "B2",
        "topic": "conditionals"
    },
    {
        "template": "{s} ____ English for three years.",
        "options": ["has studied", "studied", "studies", "study"],
        "correct": "has studied",
        "difficulty": "B1",
        "topic": "present perfect"
    },
]

phrasal_verbs = [
    {
        "question": "The meeting was ____ because the manager was ill.",
        "options": ["called off", "called up", "called in", "called on"],
        "correct": "called off",
        "difficulty": "B2",
        "topic": "phrasal verbs"
    },
    {
        "question": "She decided to ____ smoking.",
        "options": ["give up", "give in", "give away", "give off"],
        "correct": "give up",
        "difficulty": "B1",
        "topic": "phrasal verbs"
    }
]

collocations = [
    {
        "question": "She has a ____ knowledge of linguistics.",
        "options": ["broad", "large", "big", "wide"],
        "correct": "broad",
        "difficulty": "C1",
        "topic": "collocations"
    },
    {
        "question": "He made a ____ decision.",
        "options": ["wise", "clever", "smart", "intelligent"],
        "correct": "wise",
        "difficulty": "B2",
        "topic": "collocations"
    }
]

advanced = [
    {
        "question": "Hardly ____ the meeting started when the alarm rang.",
        "options": ["had", "has", "did", "was"],
        "correct": "had",
        "difficulty": "C1",
        "topic": "inversion"
    },
    {
        "question": "Not until the report was published ____ the problem.",
        "options": ["did we understand", "we understood", "understood we", "we did understand"],
        "correct": "did we understand",
        "difficulty": "C2",
        "topic": "inversion"
    }
]

def generate_questions():
    generated = []

    for template in grammar_templates:
        for s in subjects:
            for v in verbs:
                q = template["template"].format(
                    s=s,
                    s_lower=s.lower(),
                    v=v
                )

                generated.append({
                    "question": q,
                    "options": template["options"],
                    "correct": template["correct"],
                    "difficulty": template["difficulty"],
                    "topic": template["topic"]
                })

    generated.extend(phrasal_verbs)
    generated.extend(collocations)
    generated.extend(advanced)

    return generated


def seed():
    db = SessionLocal()

    questions = generate_questions()

    for q in questions:
        db.add(QuestionBank(**q))

    db.commit()
    db.close()

    print(f"{len(questions)} questions inserted")


if __name__ == "__main__":
    seed()