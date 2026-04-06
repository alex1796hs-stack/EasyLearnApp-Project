from app.database import SessionLocal
from app.models.question_bank import QuestionBank

questions = [
    # Unit 1: Present Time (15 Questions)
    {
        "question": "He ____ constantly complaining about the temperature in the office, which is getting on my nerves.",
        "options": ["is", "has been", "does", "was"],
        "correct": "is",
        "difficulty": "C1",
        "topic": "present time"
    },
    {
        "question": "I ____ to understand what the lecturer is getting at, but her argument is extremely convoluted.",
        "options": ["try", "am trying", "have tried", "tries"],
        "correct": "am trying",
        "difficulty": "C1",
        "topic": "present time"
    },
    {
        "question": "By the time you finish reading this, I ____ for the airport.",
        "options": ["will have left", "will be leaving", "leave", "am leaving"],
        "correct": "am leaving",
        "difficulty": "B2",
        "topic": "present time"
    },
    {
        "question": "The board of directors ____ a meeting tomorrow at noon to discuss the merger.",
        "options": ["is having", "have", "are to have", "has"],
        "correct": "is having",
        "difficulty": "C1",
        "topic": "present time"
    },
    {
        "question": "You look absolutely exhausted! What ____ all morning?",
        "options": ["have you done", "did you do", "have you been doing", "do you do"],
        "correct": "have you been doing",
        "difficulty": "B2",
        "topic": "present time"
    },
    {
        "question": "I ____ this software for years, but I still discover new features occasionally.",
        "options": ["am using", "use", "have been using", "have used"],
        "correct": "have been using",
        "difficulty": "C1",
        "topic": "present time"
    },
    {
        "question": "The package ____ to contain highly sensitive documents.",
        "options": ["appears", "is appearing", "has appeared", "appear"],
        "correct": "appears",
        "difficulty": "C1",
        "topic": "present time"
    },
    {
        "question": "Whenever I visit my grandmother, she ____ me stories about her youth.",
        "options": ["is telling", "tells", "has told", "telling"],
        "correct": "tells",
        "difficulty": "B1",
        "topic": "present time"
    },
    {
        "question": "To be honest, I ____ that your proposal is the most viable option we have.",
        "options": ["am thinking", "have thought", "think", "was thinking"],
        "correct": "think",
        "difficulty": "C1",
        "topic": "present time"
    },
    {
        "question": "Don't bother calling her now; she ____ an interview and won't answer.",
        "options": ["has", "is having", "has had", "will have"],
        "correct": "is having",
        "difficulty": "B2",
        "topic": "present time"
    },
    {
        "question": "She ____ her keys! This is the third time this week.",
        "options": ["has lost", "is losing", "loses", "has been losing"],
        "correct": "has lost",
        "difficulty": "B2",
        "topic": "present time"
    },
    {
        "question": "Water ____ at 100 degrees Celsius under standard atmospheric pressure.",
        "options": ["is boiling", "boil", "has boiled", "boils"],
        "correct": "boils",
        "difficulty": "A2",
        "topic": "present time"
    },
    {
        "question": "My car broke down, so I ____ my brother's vehicle until mine is repaired.",
        "options": ["use", "have used", "am using", "will use"],
        "correct": "am using",
        "difficulty": "B2",
        "topic": "present time"
    },
    {
        "question": "In the final act of the play, the protagonist ____ the truth about his lineage.",
        "options": ["is discovering", "discover", "discovers", "has discovered"],
        "correct": "discovers",
        "difficulty": "C1",
        "topic": "present time"
    },
    {
        "question": "It ____ that the company will announce significant layoffs next quarter.",
        "options": ["is believed", "believes", "is believing", "has believed"],
        "correct": "is believed",
        "difficulty": "C2",
        "topic": "present time"
    }
]

def seed_questions():
    db = SessionLocal()

    # Clear old identical topic questions to prevent massive duplicates on reload
    db.query(QuestionBank).filter(QuestionBank.topic == "present time").delete()
    db.commit()

    for q in questions:
        question = QuestionBank(**q)
        db.add(question)

    db.commit()
    db.close()

    print(f"{len(questions)} questions inserted successfully")

if __name__ == "__main__":
    seed_questions()