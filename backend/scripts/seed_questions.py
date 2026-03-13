from app.database import SessionLocal
from app.models.question_bank import QuestionBank

questions = [

# A2
{
"question": "I ____ to London last year.",
"options": ["go", "went", "gone", "going"],
"correct": "went",
"difficulty": "A2",
"topic": "past simple"
},

{
"question": "She ____ English every day.",
"options": ["study", "studies", "studied", "studying"],
"correct": "studies",
"difficulty": "A2",
"topic": "present simple"
},

{
"question": "You ____ smoke here.",
"options": ["mustn't", "can", "should", "might"],
"correct": "mustn't",
"difficulty": "A2",
"topic": "modals"
},

# B1
{
"question": "She ____ been studying English for three years.",
"options": ["has", "have", "had", "having"],
"correct": "has",
"difficulty": "B1",
"topic": "present perfect"
},

{
"question": "The meeting was cancelled ____ the bad weather.",
"options": ["because", "because of", "although", "despite"],
"correct": "because of",
"difficulty": "B1",
"topic": "connectors"
},

{
"question": "The book ____ by millions of people.",
"options": ["read", "reads", "is read", "reading"],
"correct": "is read",
"difficulty": "B1",
"topic": "passive voice"
},

# B2
{
"question": "If I ____ more time, I would travel more.",
"options": ["have", "had", "will have", "having"],
"correct": "had",
"difficulty": "B2",
"topic": "conditionals"
},

{
"question": "He suggested ____ to the cinema.",
"options": ["go", "to go", "going", "gone"],
"correct": "going",
"difficulty": "B2",
"topic": "gerunds"
},

{
"question": "By the time we arrived, they ____ already left.",
"options": ["have", "had", "has", "having"],
"correct": "had",
"difficulty": "B2",
"topic": "past perfect"
},

# C1
{
"question": "Hardly ____ the meeting started when the fire alarm rang.",
"options": ["had", "has", "did", "was"],
"correct": "had",
"difficulty": "C1",
"topic": "inversion"
},

{
"question": "She has a very ____ knowledge of linguistics.",
"options": ["wide", "broad", "large", "big"],
"correct": "broad",
"difficulty": "C1",
"topic": "collocations"
},

{
"question": "The CEO decided to ____ the proposal after careful consideration.",
"options": ["carry out", "turn down", "bring about", "take up"],
"correct": "turn down",
"difficulty": "C1",
"topic": "phrasal verbs"
},

{
"question": "The results were completely ____ our expectations.",
"options": ["beyond", "over", "above", "outside"],
"correct": "beyond",
"difficulty": "C1",
"topic": "expressions"
},

# C2
{
"question": "Not until the report was published ____ the scale of the problem.",
"options": ["did we realize", "we realized", "realized we", "we did realize"],
"correct": "did we realize",
"difficulty": "C2",
"topic": "advanced inversion"
},

{
"question": "His explanation was so ____ that nobody could challenge it.",
"options": ["cogent", "obvious", "clear", "plain"],
"correct": "cogent",
"difficulty": "C2",
"topic": "advanced vocabulary"
},

{
"question": "The theory has been widely ____ by leading academics.",
"options": ["refuted", "broken", "damaged", "crashed"],
"correct": "refuted",
"difficulty": "C2",
"topic": "academic vocabulary"
},

{
"question": "The politician tried to ____ the issue during the debate.",
"options": ["sidestep", "step aside", "walk away", "pass over"],
"correct": "sidestep",
"difficulty": "C2",
"topic": "advanced verbs"
},

{
"question": "Only after several months ____ the complexity of the task.",
"options": ["did she understand", "she understood", "understood she", "she did understand"],
"correct": "did she understand",
"difficulty": "C2",
"topic": "inversion"
}

]

def seed_questions():
    db = SessionLocal()

    for q in questions:
        question = QuestionBank(**q)
        db.add(question)

    db.commit()
    db.close()

    print("Questions inserted successfully")

if __name__ == "__main__":
    seed_questions()