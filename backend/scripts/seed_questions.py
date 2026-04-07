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
    },

    # Unit 2: Thinking and Learning (15 Questions - Vocabulary)
    {
        "question": "It takes a while to ____ all the information in a long lecture.",
        "options": ["take in", "take up", "take off", "take over"],
        "correct": "take in",
        "difficulty": "B2",
        "topic": "thinking and learning"
    },
    {
        "question": "She has a remarkable ability to ____ new facts quickly.",
        "options": ["retain", "remain", "refrain", "regain"],
        "correct": "retain",
        "difficulty": "C1",
        "topic": "thinking and learning"
    },
    {
        "question": "We need to ____ how to solve this problem before the deadline.",
        "options": ["figure out", "find out", "give up", "make up"],
        "correct": "figure out",
        "difficulty": "B1",
        "topic": "thinking and learning"
    },
    {
        "question": "He ____ Spanish very quickly while living in Madrid.",
        "options": ["picked up", "picked off", "picked out", "picked over"],
        "correct": "picked up",
        "difficulty": "B2",
        "topic": "thinking and learning"
    },
    {
        "question": "If you want to pass, you'll have to learn this poem ____.",
        "options": ["by heart", "by hand", "by mind", "by head"],
        "correct": "by heart",
        "difficulty": "A2",
        "topic": "thinking and learning"
    },
    {
        "question": "Success in this field requires a high level of ____ skill.",
        "options": ["cognitive", "content", "condition", "context"],
        "correct": "cognitive",
        "difficulty": "C1",
        "topic": "thinking and learning"
    },
    {
        "question": "She is making excellent ____ in her piano lessons.",
        "options": ["progress", "process", "program", "project"],
        "correct": "progress",
        "difficulty": "B1",
        "topic": "thinking and learning"
    },
    {
        "question": "He decided to ____ into the effects of climate change.",
        "options": ["do research", "make research", "have research", "get research"],
        "correct": "do research",
        "difficulty": "B2",
        "topic": "thinking and learning"
    },
    {
        "question": "After years of practice, he finally ____ enough experience to lead the team.",
        "options": ["gained", "won", "earned", "made"],
        "correct": "gained",
        "difficulty": "C1",
        "topic": "thinking and learning"
    },
    {
        "question": "She is such a ____ learner; she understands everything the first time.",
        "options": ["quick", "fast", "swift", "rapid"],
        "correct": "quick",
        "difficulty": "A2",
        "topic": "thinking and learning"
    },
    {
        "question": "The main ____ of the experiment was to test the hypothesis.",
        "options": ["objective", "objection", "observer", "obstacle"],
        "correct": "objective",
        "difficulty": "B2",
        "topic": "thinking and learning"
    },
    {
        "question": "Studying abroad can help you ____ a new perspective on life.",
        "options": ["acquire", "require", "inquire", "inspire"],
        "correct": "acquire",
        "difficulty": "C1",
        "topic": "thinking and learning"
    },
    {
        "question": "He is a fast ____ and always gets the highest marks.",
        "options": ["learner", "learning", "learned", "learns"],
        "correct": "learner",
        "difficulty": "A2",
        "topic": "thinking and learning"
    },
    {
        "question": "The ____ process can be difficult but rewarding.",
        "options": ["learning", "learner", "learned", "learns"],
        "correct": "learning",
        "difficulty": "A1",
        "topic": "thinking and learning"
    },
    {
        "question": "I can't ____ the name of that actor right now.",
        "options": ["recall", "remind", "record", "repeat"],
        "correct": "recall",
        "difficulty": "B2",
        "topic": "thinking and learning"
    },

    # Unit 3: Past Time (15 Questions)
    {
        "question": "By the time the paramedics arrived, the building ____ completely.",
        "options": ["collapsed", "had collapsed", "has collapsed", "was collapsing"],
        "correct": "had collapsed",
        "difficulty": "C1",
        "topic": "past time"
    },
    {
        "question": "I ____ about calling you all day yesterday, but I never got around to it.",
        "options": ["thought", "was thinking", "had thought", "had been thinking"],
        "correct": "was thinking",
        "difficulty": "B2",
        "topic": "past time"
    },
    {
        "question": "As a child, I ____ spend hours playing in the woods behind our house.",
        "options": ["used to", "would", "both are correct", "none are correct"],
        "correct": "both are correct",
        "difficulty": "C1",
        "topic": "past time"
    },
    {
        "question": "She ____ at the company for over twenty years before she finally decided to retire.",
        "options": ["worked", "was working", "had worked", "had been working"],
        "correct": "had been working",
        "difficulty": "C1",
        "topic": "past time"
    },
    {
        "question": "He was breathless because he ____ all the way from the station.",
        "options": ["ran", "was running", "had run", "had been running"],
        "correct": "had been running",
        "difficulty": "B2",
        "topic": "past time"
    },
    {
        "question": "Little ____ we know that our lives were about to change forever.",
        "options": ["did", "had", "would", "do"],
        "correct": "did",
        "difficulty": "C2",
        "topic": "past time"
    },
    {
        "question": "Hardly ____ the meeting started when the fire alarm went off.",
        "options": ["did", "has", "had", "was"],
        "correct": "had",
        "difficulty": "C1",
        "topic": "past time"
    },
    {
        "question": "I ____ my keys four times already this month; I really must be more careful.",
        "options": ["lost", "was losing", "had lost", "have lost"],
        "correct": "have lost",
        "difficulty": "B1",
        "topic": "past time"
    },
    {
        "question": "When I was younger, I ____ like spinach, but now I love it.",
        "options": ["didn't used to", "didn't use to", "wouldn't", "hadn't"],
        "correct": "didn't use to",
        "difficulty": "B2",
        "topic": "past time"
    },
    {
        "question": "The detective noticed that someone ____ the lock on the safe.",
        "options": ["tampered", "was tampering", "had tampered", "had been tampering"],
        "correct": "had tampered",
        "difficulty": "C1",
        "topic": "past time"
    },
    {
        "question": "It was the first time she ____ such an impressive performance.",
        "options": ["saw", "was seeing", "had seen", "has seen"],
        "correct": "had seen",
        "difficulty": "C1",
        "topic": "past time"
    },
    {
        "question": "They ____ for three hours when it finally started to rain.",
        "options": ["drove", "were driving", "had driven", "had been driving"],
        "correct": "had been driving",
        "difficulty": "B2",
        "topic": "past time"
    },
    {
        "question": "I ____ to the cinema last night with some old friends from university.",
        "options": ["go", "went", "had gone", "was going"],
        "correct": "went",
        "difficulty": "A2",
        "topic": "past time"
    },
    {
        "question": "No sooner ____ the plane touched down than the passengers began to unbuckle their seatbelts.",
        "options": ["did", "has", "had", "was"],
        "correct": "had",
        "difficulty": "C2",
        "topic": "past time"
    },
    {
        "question": "At that time, the company ____ through a period of rapid expansion.",
        "options": ["went", "was going", "had gone", "had been going"],
        "correct": "was going",
        "difficulty": "B2",
        "topic": "past time"
    }
]

def seed_questions():
    db = SessionLocal()

    # Clear old questions for topics we are about to seed
    topics = set(q["topic"] for q in questions)
    for t in topics:
        db.query(QuestionBank).filter(QuestionBank.topic == t).delete()
    
    db.commit()

    for q in questions:
        question = QuestionBank(**q)
        db.add(question)

    db.commit()
    db.close()

    print(f"{len(questions)} questions inserted successfully")

if __name__ == "__main__":
    seed_questions()