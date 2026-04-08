import json
from app.database import SessionLocal
from app.models.lesson import Lesson
from app.models.lesson_content import LessonContent

def generate_content(topic):
    # -----------------------
    # GRAMMAR: Present Time (Unit 1)
    # -----------------------
    if topic == "present time":
        return [
            {"type": "intro", "order": 1, "title": "1. Present Simple",
             "explanation": "We use the present simple for:\n• General truths and facts (Water boils at 100°C).\n• Current habits and routines (He always takes the bus).\n• Permanent situations and states (I live in London).\n• Timetables and scheduled events (The train leaves at 5 PM).\n• Reviews, commentaries and dramatic narratives."},
            {"type": "concept", "order": 2, "title": "2. Present Continuous",
             "explanation": "We use the present continuous for:\n• Actions happening right now (She is studying).\n• Temporary situations (I'm living with my parents until I find a flat).\n• Changing/developing situations (The climate is getting warmer).\n• Annoying habits with 'always' (You are always forgetting your keys!).\n• Definite future arrangements (We are meeting John tonight)."},
            {"type": "concept", "order": 3, "title": "3. Present Perfect Simple",
             "explanation": "We use the present perfect simple for:\n• Actions at an unspecified time in the past (I have been to Paris).\n• Actions that started in the past and continue to the present (I have known him for years).\n• Past actions with a visible present result (She has broken her leg).\n• Experiences up to now, often with 'ever' or 'never'."},
            {"type": "concept", "order": 4, "title": "4. Present Perfect Continuous",
             "explanation": "We use the present perfect continuous for:\n• Actions started in the past still in progress, emphasizing duration (I have been studying all day).\n• Actions recently stopped with visible results (You look tired. Have you been running?).\n• Note: We cannot use continuous tenses with stative verbs (know, like, believe)."},
            {"type": "advanced", "order": 5, "title": "5. Stative Verbs",
             "explanation": "Stative verbs describe states and are not typically used in continuous tenses.\n• Thoughts: believe, know, understand, think (opinion).\n• Senses: hear, see, smell, taste, feel.\n• Emotions: love, hate, like, prefer.\n• Possession: have, own, belong.\n\nSome verbs can be both stative and dynamic with different meanings:\n- I think it's good. (opinion) vs I am thinking about it. (mental process)"}
        ]

    # -----------------------
    # VOCABULARY: Thinking & Learning (Unit 2)
    # -----------------------
    if topic == "thinking and learning":
        return [
            {"type": "vocabulary", "order": 1, "title": "Topic Vocabulary",
             "explanation": "Key terms: acquire knowledge, retain information, cognitive skills, intellectually stimulating, thought-provoking, lateral thinking, analytical skills."},
            {"type": "vocabulary", "order": 2, "title": "Phrasal Verbs",
             "explanation": "• figure out = understand after thinking\n• pick up = learn informally\n• take in = absorb information\n• read up on = research thoroughly\n• catch on = understand eventually\n• swot up = study intensively"},
            {"type": "vocabulary", "order": 3, "title": "Collocations",
             "explanation": "• make progress / make an effort\n• do research / do an experiment\n• gain experience / gain knowledge\n• broaden your horizons\n• meet a deadline"},
            {"type": "vocabulary", "order": 4, "title": "Idioms",
             "explanation": "• learn by heart = memorize\n• a quick/slow learner\n• get the hang of = become competent\n• know something inside out\n• have a mind like a sieve = forget easily"},
            {"type": "vocabulary", "order": 5, "title": "Word Formation",
             "explanation": "• learn → learner → learning → learned/learnt\n• know → knowledge → knowledgeable\n• educate → education → educational → educator\n• analyse → analysis → analytical → analyst"}
        ]

    # -----------------------
    # GRAMMAR: Past Time (Unit 3)
    # -----------------------
    if topic == "past time":
        return [
            {"type": "intro", "order": 1, "title": "Understanding Past Time",
             "explanation": "Past time forms describe actions and situations that happened before now. The correct tense depends on whether the action was completed, in progress, or happened before another past action."},
            {"type": "concept", "order": 2, "title": "Past Simple",
             "explanation": "Used for completed actions in the past, often with time expressions.\nExample: She finished her homework before dinner.\nExample: I visited Rome in 2019."},
            {"type": "concept", "order": 3, "title": "Past Continuous",
             "explanation": "Used for actions in progress at a specific past moment, or background actions.\nExample: I was studying when he called.\nExample: While she was cooking, the phone rang."},
            {"type": "concept", "order": 4, "title": "Past Perfect",
             "explanation": "Used for actions completed before another past action.\nExample: She had already left when I arrived.\nExample: By the time we got there, the film had started."},
            {"type": "comparison", "order": 5, "title": "Past Simple vs Continuous",
             "explanation": "Past Simple = completed action. Past Continuous = action in progress.\n• I watched TV when she called. (I stopped to answer)\n• I was watching TV when she called. (I was in the middle of watching)"},
            {"type": "advanced", "order": 6, "title": "Past Perfect Continuous",
             "explanation": "Used to emphasise duration before another past event.\nExample: I had been waiting for hours before they arrived.\nExample: She had been working there for 20 years before she retired."}
        ]

    # -----------------------
    # VOCABULARY: Change & Technology (Unit 4)
    # -----------------------
    if topic == "change and technology":
        return [
            {"type": "vocabulary", "order": 1, "title": "Topic Vocabulary",
             "explanation": "Key terms: adapt, adjust, alter, amend, convert, modify, mutate, transform, revolutionise, innovate, upgrade, update."},
            {"type": "vocabulary", "order": 2, "title": "Phrasal Verbs",
             "explanation": "• back up = make a copy of data\n• break down = stop functioning\n• key in = type/enter data\n• change around = rearrange\n• use up = consume completely\n• wear out = become unusable through use"},
            {"type": "vocabulary", "order": 3, "title": "Collocations & Phrases",
             "explanation": "• a change of heart = change your mind\n• a leap in the dark = risky decision\n• break with tradition\n• keep up with the times\n• state-of-the-art technology"},
            {"type": "vocabulary", "order": 4, "title": "Idioms",
             "explanation": "• reinvent the wheel = waste time doing what's already done\n• turn over a new leaf = start fresh\n• change your tune = change your opinion\n• a change is as good as a rest"},
            {"type": "vocabulary", "order": 5, "title": "Word Formation",
             "explanation": "• adapt → adaptation → adaptable → adaptability\n• adjust → adjustment → adjustable\n• alter → alteration → unalterable\n• innovate → innovation → innovative → innovator"}
        ]

    # -----------------------
    # GRAMMAR: Future Time (Unit 5)
    # -----------------------
    if topic == "future time":
        return [
            {"type": "intro", "order": 1, "title": "Exploring Future Time",
             "explanation": "English has multiple ways to express the future, each with specific nuances. At C1/C2 level, mastering the differences is essential."},
            {"type": "concept", "order": 2, "title": "Future Continuous",
             "explanation": "Action in progress at a specific time in the future.\nExample: This time tomorrow, I will be flying to New York.\nAlso used for polite enquiries: Will you be attending the meeting?"},
            {"type": "concept", "order": 3, "title": "Future Perfect Simple",
             "explanation": "Action completed by a point in the future.\nExample: I will have finished my PhD by June.\nExample: By next year, they will have built the new bridge."},
            {"type": "concept", "order": 4, "title": "Future Perfect Continuous",
             "explanation": "Duration of an action up to a point in the future.\nExample: By 2030, I will have been living here for 10 years.\nExample: Next month, she will have been working here for five years."},
            {"type": "advanced", "order": 5, "title": "Other Future Expressions",
             "explanation": "• be about to / on the point of = imminent action\n• be due to = scheduled/expected (formal)\n• be to = official arrangements\n• be bound to / be sure to = certainty\nExample: The president is to give a speech at the ceremony."}
        ]

    # -----------------------
    # VOCABULARY: Time & Work (Unit 6)
    # -----------------------
    if topic == "time and work":
        return [
            {"type": "vocabulary", "order": 1, "title": "Topic Vocabulary",
             "explanation": "Key terms: commute, resign, retire, promote, recruit, dismiss, make redundant, freelance, overtime, shift work, career ladder, appraisal, deadline."},
            {"type": "vocabulary", "order": 2, "title": "Phrasal Verbs",
             "explanation": "• take on = employ / accept responsibility\n• lay off = make redundant\n• hand in = submit (resignation)\n• set up = start (a business)\n• knuckle down = start working hard\n• slack off = work less hard"},
            {"type": "vocabulary", "order": 3, "title": "Collocations",
             "explanation": "• meet a deadline / miss a deadline\n• do overtime / work shifts\n• job satisfaction / job security\n• fringe benefits / perks of the job\n• make a living / earn a salary"},
            {"type": "vocabulary", "order": 4, "title": "Idioms",
             "explanation": "• work against the clock = rush to finish\n• get the sack = be fired\n• burn the midnight oil = work late\n• a dead-end job = no promotion prospects\n• pull your weight = do your fair share"},
            {"type": "vocabulary", "order": 5, "title": "Word Formation",
             "explanation": "• employ → employer → employee → employment → unemployment\n• promote → promotion → promotional\n• occupy → occupation → occupational\n• retire → retirement → retiree"}
        ]

    # -----------------------
    # GRAMMAR: Passives & Causatives (Unit 7)
    # -----------------------
    if topic == "passives and causatives":
        return [
            {"type": "intro", "order": 1, "title": "The Passive Voice",
             "explanation": "We use the passive when the action is more important than who does it, or when the agent is unknown.\nActive: Someone stole my car.\nPassive: My car was stolen."},
            {"type": "concept", "order": 2, "title": "Passive Forms Across Tenses",
             "explanation": "• Present Simple: The report is written every week.\n• Past Simple: The building was constructed in 1990.\n• Present Perfect: The project has been completed.\n• Future: The results will be announced tomorrow.\n• Modal: This problem can be solved easily."},
            {"type": "concept", "order": 3, "title": "Advanced Passive Structures",
             "explanation": "• It is said/believed/thought that... (impersonal passive)\n• He is said to be very rich. (personal passive)\n• Having been warned, she stayed away.\n• The house needs painting. (passive gerund)"},
            {"type": "concept", "order": 4, "title": "Causative Have/Get",
             "explanation": "Used when someone else does something for you.\n• have + object + past participle: I had my hair cut.\n• get + object + past participle: I got my car repaired.\n• have + someone + infinitive: I'll have the technician check it.\n• get + someone + to infinitive: I got him to fix it."},
            {"type": "advanced", "order": 5, "title": "Passives with Reporting Verbs",
             "explanation": "• It is reported that the president will resign.\n• The president is reported to be considering resignation.\n• Common verbs: say, believe, expect, know, think, consider, allege, claim, understand."}
        ]

    # -----------------------
    # VOCABULARY: Movement & Transport (Unit 8)
    # -----------------------
    if topic == "movement and transport":
        return [
            {"type": "vocabulary", "order": 1, "title": "Topic Vocabulary",
             "explanation": "Key terms: commute, congestion, fare, pedestrian, junction, bypass, carriageway, overtake, accelerate, cruise, embark, disembark."},
            {"type": "vocabulary", "order": 2, "title": "Phrasal Verbs",
             "explanation": "• pull over = stop at the side of the road\n• break down = stop working (vehicle)\n• set off / set out = begin a journey\n• pick up = collect someone\n• drop off = leave someone somewhere\n• run over = hit with a vehicle"},
            {"type": "vocabulary", "order": 3, "title": "Collocations",
             "explanation": "• catch / miss a train / flight\n• heavy / light traffic\n• rush hour / peak time\n• long-haul / short-haul flight\n• give someone a lift/ride"},
            {"type": "vocabulary", "order": 4, "title": "Idioms",
             "explanation": "• hit the road = start travelling\n• in the fast lane = living an exciting life\n• at a crossroads = at a decision point\n• a bumpy ride = a difficult experience\n• road rage = anger while driving"},
            {"type": "vocabulary", "order": 5, "title": "Word Formation",
             "explanation": "• depart → departure → departed\n• arrive → arrival\n• travel → traveller → travelling\n• navigate → navigation → navigator"}
        ]

    # -----------------------
    # GRAMMAR: Modals & Semi-modals (Unit 9)
    # -----------------------
    if topic == "modals":
        return [
            {"type": "intro", "order": 1, "title": "Modal Verbs Overview",
             "explanation": "Modal verbs (can, could, may, might, must, shall, should, will, would) modify the meaning of the main verb to express ability, possibility, permission, obligation, or deduction."},
            {"type": "concept", "order": 2, "title": "Obligation & Necessity",
             "explanation": "• must = strong obligation (I must finish this today)\n• have to = external obligation (I have to wear a uniform)\n• need to = necessity (You need to register first)\n• should/ought to = advice/recommendation\n• had better = strong advice with warning"},
            {"type": "concept", "order": 3, "title": "Ability & Permission",
             "explanation": "• can/could = general ability (I can swim)\n• be able to = specific achievement (I was able to escape)\n• may/can = permission (May I leave early?)\n• be allowed to = formal permission\n• could = past ability (I could run fast as a child)"},
            {"type": "concept", "order": 4, "title": "Deduction & Speculation",
             "explanation": "• must = certain deduction (He must be at home, his car is here)\n• can't = impossible (She can't be 60, she looks so young)\n• may/might/could = possibility (It might rain later)\n• must have + pp = past certainty (He must have forgotten)\n• can't have + pp = past impossibility"},
            {"type": "advanced", "order": 5, "title": "Semi-modals & Advanced Uses",
             "explanation": "Semi-modals behave partly like modals:\n• dare (I dare say / How dare you!)\n• need (Need I say more? / You needn't worry)\n• used to (I used to live there)\n\nCriticism of past actions:\n• should have + pp: You should have told me.\n• needn't have + pp: You needn't have brought a gift."}
        ]

    # -----------------------
    # VOCABULARY: Communication & Media (Unit 10)
    # -----------------------
    if topic == "communication":
        return [
            {"type": "vocabulary", "order": 1, "title": "Topic Vocabulary",
             "explanation": "Key terms: broadcast, circulation, correspondent, coverage, editorial, headline, readership, tabloid, broadsheet, bulletin, podcast, streaming."},
            {"type": "vocabulary", "order": 2, "title": "Phrasal Verbs",
             "explanation": "• come across = find by chance / give an impression\n• get through = reach by phone\n• put across = communicate an idea\n• speak up = talk louder / express opinion\n• turn down = reduce volume / reject\n• tune in = watch/listen to a broadcast"},
            {"type": "vocabulary", "order": 3, "title": "Collocations",
             "explanation": "• break the news = tell important news\n• make headlines = be in the news\n• hold a conversation\n• spread the word = tell people\n• keep in touch / lose touch"},
            {"type": "vocabulary", "order": 4, "title": "Idioms",
             "explanation": "• hit the headlines = become major news\n• get the message = understand\n• read between the lines = understand hidden meaning\n• be on the same wavelength = think alike\n• the grapevine = informal communication"},
            {"type": "vocabulary", "order": 5, "title": "Word Formation",
             "explanation": "• communicate → communication → communicative → communicator\n• inform → information → informative → misinformation\n• advertise → advertisement → advertiser → advertising\n• publish → publication → publisher → publishing"}
        ]

    # -----------------------
    # GRAMMAR: Conditionals (Unit 11)
    # -----------------------
    if topic == "conditionals":
        return [
            {"type": "intro", "order": 1, "title": "Conditional Structures Overview",
             "explanation": "Conditionals express hypothetical situations and their consequences. At C1/C2, you must master mixed conditionals and alternatives to 'if'."},
            {"type": "concept", "order": 2, "title": "Zero & First Conditional",
             "explanation": "Zero: If + present, present (general truths).\n• If you heat water to 100°C, it boils.\n\nFirst: If + present, will + infinitive (real/likely future).\n• If it rains, we'll stay inside.\n• Unless you hurry, you'll miss the train."},
            {"type": "concept", "order": 3, "title": "Second & Third Conditional",
             "explanation": "Second: If + past simple, would + infinitive (unreal present/future).\n• If I had more time, I would travel.\n\nThird: If + past perfect, would have + pp (unreal past).\n• If I had studied harder, I would have passed."},
            {"type": "concept", "order": 4, "title": "Mixed Conditionals",
             "explanation": "Past condition → present result:\n• If I had taken that job, I would be living in Paris now.\n\nPresent condition → past result:\n• If she weren't so shy, she would have spoken up at the meeting."},
            {"type": "advanced", "order": 5, "title": "Alternatives to 'If'",
             "explanation": "• provided/providing (that) = on condition that\n• as/so long as = only if\n• supposing / suppose = what if\n• on condition that = formal if\n• but for = if it weren't for\n• otherwise = if not\n• Were I to... / Had I known... (formal inversion)"}
        ]

    # -----------------------
    # VOCABULARY: Chance & Nature (Unit 12)
    # -----------------------
    if topic == "chance and nature":
        return [
            {"type": "vocabulary", "order": 1, "title": "Topic Vocabulary",
             "explanation": "Key terms: drought, flood, earthquake, eruption, hurricane, habitat, ecosystem, endangered, extinct, biodiversity, conservation, sustainable."},
            {"type": "vocabulary", "order": 2, "title": "Phrasal Verbs",
             "explanation": "• break out = start suddenly (fire, disease)\n• wipe out = destroy completely\n• die out = become extinct\n• come about = happen\n• crop up = appear unexpectedly\n• turn out = result/end up being"},
            {"type": "vocabulary", "order": 3, "title": "Collocations",
             "explanation": "• natural disaster / natural habitat\n• climate change / global warming\n• carbon footprint / carbon emissions\n• renewable energy / fossil fuels\n• take a chance / by chance / stand a chance"},
            {"type": "vocabulary", "order": 4, "title": "Idioms",
             "explanation": "• a force of nature = very powerful person\n• leave nothing to chance = be very careful\n• the calm before the storm\n• weather the storm = survive a difficult period\n• once in a blue moon = very rarely"},
            {"type": "vocabulary", "order": 5, "title": "Word Formation",
             "explanation": "• destroy → destruction → destructive → indestructible\n• conserve → conservation → conservationist\n• pollute → pollution → pollutant → polluter\n• sustain → sustainable → sustainability → unsustainable"}
        ]

    # -----------------------
    # GRAMMAR: Unreal Time (Unit 13)
    # -----------------------
    if topic == "unreal time":
        return [
            {"type": "intro", "order": 1, "title": "Understanding Unreal Time",
             "explanation": "Unreal time uses past tenses to talk about hypothetical, imaginary or wished-for situations. This includes wish, if only, it's time, would rather, and as if/as though."},
            {"type": "concept", "order": 2, "title": "Wish & If Only",
             "explanation": "Present regret: I wish I knew the answer. (but I don't)\nPast regret: I wish I had studied harder. (but I didn't)\nFuture desire: I wish you would stop making noise.\n\n'If only' is more emphatic: If only I had listened to you!"},
            {"type": "concept", "order": 3, "title": "It's (High/About) Time",
             "explanation": "Used to say something should happen now or should have happened already.\n• It's time we left. (= we should leave now)\n• It's high time you got a job. (strong criticism)\n• It's about time they did something about it."},
            {"type": "concept", "order": 4, "title": "Would Rather & Would Sooner",
             "explanation": "Preference about yourself: I'd rather stay home. (+ infinitive)\nPreference about others: I'd rather you didn't smoke here. (+ past tense)\n• I'd sooner walk than take the bus."},
            {"type": "advanced", "order": 5, "title": "As If / As Though / Suppose",
             "explanation": "To describe something that appears to be true but isn't:\n• He talks as if he were the boss. (but he isn't)\n• She looked as though she had been crying.\n• Suppose you won the lottery, what would you do?\n\nNote: 'were' is used instead of 'was' in formal English for all persons."}
        ]

    # -----------------------
    # VOCABULARY: Quantity & Money (Unit 14)
    # -----------------------
    if topic == "quantity and money":
        return [
            {"type": "vocabulary", "order": 1, "title": "Topic Vocabulary",
             "explanation": "Key terms: income, expenditure, budget, currency, inflation, interest rate, mortgage, debt, savings, investment, profit, revenue, turnover."},
            {"type": "vocabulary", "order": 2, "title": "Phrasal Verbs",
             "explanation": "• save up = collect money over time\n• pay off = finish paying a debt\n• come to = total (amount)\n• cut back on = reduce spending\n• rip off = charge too much\n• fork out = pay reluctantly"},
            {"type": "vocabulary", "order": 3, "title": "Collocations",
             "explanation": "• make a profit / make a loss\n• go bankrupt / go into debt\n• cost a fortune / cost an arm and a leg\n• a large/small amount of\n• value for money / a bargain"},
            {"type": "vocabulary", "order": 4, "title": "Idioms",
             "explanation": "• money doesn't grow on trees = money is limited\n• break the bank = cost too much\n• tighten your belt = spend less\n• make ends meet = have just enough money\n• be worth its weight in gold = very valuable"},
            {"type": "vocabulary", "order": 5, "title": "Word Formation",
             "explanation": "• invest → investment → investor → reinvest\n• economy → economic → economical → economist → economise\n• value → valuable → invaluable → valueless → devalue\n• finance → financial → financially → financier"}
        ]

    # -----------------------
    # GRAMMAR: Adjectives & Adverbs (Unit 15)
    # -----------------------
    if topic == "adjectives and adverbs":
        return [
            {"type": "intro", "order": 1, "title": "Adjectives & Adverbs Overview",
             "explanation": "At C1/C2 level, mastering the nuances of adjective order, gradability, and adverb placement is crucial for natural-sounding English."},
            {"type": "concept", "order": 2, "title": "Adjective Order",
             "explanation": "When multiple adjectives modify a noun, they follow this order:\nOpinion → Size → Age → Shape → Colour → Origin → Material → Purpose\n\nExample: A beautiful large old rectangular brown Italian wooden writing desk."},
            {"type": "concept", "order": 3, "title": "Gradable vs Ungradable Adjectives",
             "explanation": "Gradable (can be modified with very/quite): big, cold, interesting.\nUngradable (absolute): dead, unique, perfect, impossible.\n\nUse 'absolutely/utterly' with ungradable: absolutely fantastic.\nUse 'very/extremely' with gradable: very interesting.\nNever say: very fantastic ✗ / absolutely big ✗"},
            {"type": "concept", "order": 4, "title": "Comparative & Superlative Structures",
             "explanation": "Advanced patterns:\n• The more... the more: The harder you work, the more you earn.\n• by far the best / easily the worst\n• nowhere near as good as\n• not nearly as expensive as\n• considerably / slightly / marginally better than"},
            {"type": "advanced", "order": 5, "title": "Adverb Position & Meaning",
             "explanation": "Position can change meaning:\n• He simply explained the problem. (= in a simple way)\n• He simply doesn't understand. (= just/only)\n\nComment adverbs: Apparently, Evidently, Presumably, Supposedly.\nDegree adverbs: utterly, thoroughly, somewhat, barely, scarcely, hardly."}
        ]

    # -----------------------
    # VOCABULARY: Materials & Built Environment (Unit 16)
    # -----------------------
    if topic == "materials":
        return [
            {"type": "vocabulary", "order": 1, "title": "Topic Vocabulary",
             "explanation": "Key terms: concrete, timber, steel, brick, plaster, cement, insulation, foundation, scaffold, demolish, renovate, refurbish."},
            {"type": "vocabulary", "order": 2, "title": "Phrasal Verbs",
             "explanation": "• do up = renovate/decorate\n• pull down = demolish\n• put up = construct/build\n• knock through = remove a wall\n• fall down = collapse\n• block off = close an area"},
            {"type": "vocabulary", "order": 3, "title": "Collocations",
             "explanation": "• build from scratch = start from nothing\n• state-of-the-art facilities\n• run-down neighbourhood\n• high-rise / low-rise building\n• urban sprawl / green belt"},
            {"type": "vocabulary", "order": 4, "title": "Idioms",
             "explanation": "• hit the roof = become very angry\n• build bridges = improve relationships\n• lay the foundations = establish the basis\n• go through the roof = increase dramatically\n• a roof over your head = somewhere to live"},
            {"type": "vocabulary", "order": 5, "title": "Word Formation",
             "explanation": "• construct → construction → constructive → reconstruct\n• demolish → demolition\n• architect → architecture → architectural\n• inhabit → inhabitant → habitable → uninhabitable"}
        ]

    # -----------------------
    # GRAMMAR: Clauses (Unit 17)
    # -----------------------
    if topic == "clauses":
        return [
            {"type": "intro", "order": 1, "title": "Relative Clauses",
             "explanation": "Defining clauses give essential information (no commas):\n• The man who lives next door is a doctor.\n\nNon-defining clauses add extra information (with commas):\n• My brother, who lives in Paris, is visiting us."},
            {"type": "concept", "order": 2, "title": "Reduced Relative Clauses",
             "explanation": "We can shorten relative clauses using participles:\n• The woman sitting by the window is my aunt. (= who is sitting)\n• The letter written by hand was from my grandmother. (= which was written)"},
            {"type": "concept", "order": 3, "title": "Nominal Clauses (That/What)",
             "explanation": "Clauses acting as nouns:\n• What surprised me was his honesty.\n• That he arrived on time was remarkable.\n• It is essential that everyone attend the meeting."},
            {"type": "concept", "order": 4, "title": "Adverbial Clauses",
             "explanation": "Time: As soon as / By the time / No sooner...than\nReason: Since / As / Given that\nContrast: Although / Even though / Whereas / While\nPurpose: So that / In order that"},
            {"type": "advanced", "order": 5, "title": "Participle Clauses",
             "explanation": "• Having finished the work, she went home. (= After she had finished)\n• Not knowing what to do, I called for help.\n• Seen from above, the city looks beautiful.\n• Weather permitting, we'll have a picnic."}
        ]

    # -----------------------
    # VOCABULARY: Reactions & Health (Unit 18)
    # -----------------------
    if topic == "health":
        return [
            {"type": "vocabulary", "order": 1, "title": "Topic Vocabulary",
             "explanation": "Key terms: symptom, diagnosis, prescription, treatment, therapy, side effect, immune system, chronic, acute, contagious, epidemic, pandemic."},
            {"type": "vocabulary", "order": 2, "title": "Phrasal Verbs",
             "explanation": "• come down with = become ill\n• get over = recover from\n• pass out = faint\n• bring round = make conscious again\n• fight off = resist an illness\n• break out in = suddenly develop (rash, spots)"},
            {"type": "vocabulary", "order": 3, "title": "Collocations",
             "explanation": "• catch a cold / catch a disease\n• have an operation / have surgery\n• make a recovery / make progress\n• take medicine / take painkillers\n• run a temperature / run a fever"},
            {"type": "vocabulary", "order": 4, "title": "Idioms",
             "explanation": "• feel under the weather = feel ill\n• be on the mend = be recovering\n• a clean bill of health = confirmed healthy\n• be as fit as a fiddle = very healthy\n• go under the knife = have surgery"},
            {"type": "vocabulary", "order": 5, "title": "Word Formation",
             "explanation": "• heal → health → healthy → unhealthy → healthcare\n• treat → treatment → treatable → untreatable\n• infect → infection → infectious → disinfect\n• prescribe → prescription → prescriptive"}
        ]

    # -----------------------
    # GRAMMAR: Complex Sentences (Unit 19)
    # -----------------------
    if topic == "complex sentences":
        return [
            {"type": "intro", "order": 1, "title": "Inversion for Emphasis",
             "explanation": "We can invert subject and verb for emphasis or formality:\n• Never have I seen such beauty.\n• Rarely does he arrive on time.\n• Not only did she win, but she also broke the record.\n• Little did they know what was about to happen."},
            {"type": "concept", "order": 2, "title": "Cleft Sentences",
             "explanation": "Used to focus on a specific part of the sentence:\n• It was John who broke the window. (focus on John)\n• What I need is a good rest. (focus on 'a good rest')\n• All I want is some peace and quiet.\n• The reason why I left was the low salary."},
            {"type": "concept", "order": 3, "title": "Fronting & Postponement",
             "explanation": "Moving elements for emphasis:\n• Fronting: Brilliant though she was, she failed the test.\n• Postponement: I find it difficult to believe that he lied.\n• Extraposition: It is widely known that..."},
            {"type": "concept", "order": 4, "title": "Ellipsis & Substitution",
             "explanation": "Omitting words to avoid repetition:\n• 'Are you coming?' — 'I might.' (= I might come)\n• She can play the piano and so can I.\n• I asked her to help but she didn't want to. (= want to help)"},
            {"type": "advanced", "order": 5, "title": "Discourse Markers",
             "explanation": "Linking complex ideas:\n• As a matter of fact / In actual fact\n• As far as I'm concerned / As regards\n• On the whole / By and large\n• Nevertheless / Nonetheless\n• To all intents and purposes"}
        ]

    # -----------------------
    # VOCABULARY: Power & Social Issues (Unit 20)
    # -----------------------
    if topic == "social issues":
        return [
            {"type": "vocabulary", "order": 1, "title": "Topic Vocabulary",
             "explanation": "Key terms: inequality, discrimination, poverty, homelessness, ballot, campaign, legislation, reform, welfare, justice, corruption, bureaucracy."},
            {"type": "vocabulary", "order": 2, "title": "Phrasal Verbs",
             "explanation": "• stand for = represent / tolerate\n• bring about = cause to happen\n• clamp down on = take strict action against\n• stamp out = eliminate completely\n• stand up for = defend rights\n• come into force = become law"},
            {"type": "vocabulary", "order": 3, "title": "Collocations",
             "explanation": "• raise awareness / raise funds\n• tackle a problem / address an issue\n• break the law / enforce the law\n• human rights / civil rights\n• gap between rich and poor"},
            {"type": "vocabulary", "order": 4, "title": "Idioms",
             "explanation": "• turn a blind eye = ignore something wrong\n• have a voice = have influence\n• the powers that be = people in authority\n• fight a losing battle = try without hope\n• toe the line = follow the rules"},
            {"type": "vocabulary", "order": 5, "title": "Word Formation",
             "explanation": "• govern → government → governor → governance\n• equal → equality → inequality → equalise\n• corrupt → corruption → incorruptible\n• criminalise → crime → criminal → decriminalise"}
        ]

    # -----------------------
    # GRAMMAR: Noun Phrases (Unit 21)
    # -----------------------
    if topic == "noun phrases":
        return [
            {"type": "intro", "order": 1, "title": "Complex Noun Phrases",
             "explanation": "At C1/C2 level, building sophisticated noun phrases is key to academic and formal writing.\n• Pre-modification: adjectives, nouns as modifiers\n• Post-modification: relative clauses, prepositional phrases, participles"},
            {"type": "concept", "order": 2, "title": "Articles & Determiners",
             "explanation": "Advanced article usage:\n• The + adjective = group (the rich, the elderly)\n• Zero article with abstract nouns (Freedom is precious)\n• a/an for classification (She's a doctor)\n• the for unique things (the sun, the internet)\n• Determiners: each, every, either, neither, all, both"},
            {"type": "concept", "order": 3, "title": "Quantifiers",
             "explanation": "• a great/good deal of (uncountable)\n• a large/small number of (countable)\n• plenty of / a lack of\n• the majority of / a minority of\n• each and every / one or two\n• few vs a few / little vs a little"},
            {"type": "concept", "order": 4, "title": "Possessives & Compounds",
             "explanation": "• Double genitive: a friend of John's / a painting of my mother's\n• Compound nouns: air conditioning, mother-in-law, passer-by\n• Noun + noun: bus stop, football match\n• Possessive 's vs of: the company's profits / the end of the road"},
            {"type": "advanced", "order": 5, "title": "Nominalization",
             "explanation": "Converting verbs/adjectives to nouns for formal writing:\n• They decided → Their decision\n• The system failed → The failure of the system\n• It is important → The importance of\n• We need to intervene → The need for intervention"}
        ]

    # -----------------------
    # VOCABULARY: Quality & The Arts (Unit 22)
    # -----------------------
    if topic == "arts":
        return [
            {"type": "vocabulary", "order": 1, "title": "Topic Vocabulary",
             "explanation": "Key terms: masterpiece, exhibition, sculpture, abstract, contemporary, genre, portrait, landscape, rehearsal, audition, premiere, encore."},
            {"type": "vocabulary", "order": 2, "title": "Phrasal Verbs",
             "explanation": "• take up = start a hobby\n• give up = stop doing something\n• show off = display proudly\n• bring out = release/publish\n• live up to = meet expectations\n• look up to = admire someone"},
            {"type": "vocabulary", "order": 3, "title": "Collocations",
             "explanation": "• a work of art / a piece of music\n• hold an exhibition / put on a show\n• rave reviews / mixed reviews\n• standing ovation / encore performance\n• creative talent / artistic flair"},
            {"type": "vocabulary", "order": 4, "title": "Idioms",
             "explanation": "• steal the show = be the best\n• in the limelight = centre of attention\n• behind the scenes = not visible to public\n• a tough act to follow = hard to equal\n• play it by ear = improvise"},
            {"type": "vocabulary", "order": 5, "title": "Word Formation",
             "explanation": "• create → creation → creative → creativity → creator\n• perform → performance → performer\n• exhibit → exhibition → exhibitor\n• inspire → inspiration → inspirational → uninspiring"}
        ]

    # -----------------------
    # GRAMMAR: Verbal Complements (Unit 23)
    # -----------------------
    if topic == "verbal complements":
        return [
            {"type": "intro", "order": 1, "title": "Verbs Followed by -ing or Infinitive",
             "explanation": "Some verbs take -ing, some take to-infinitive, and some take both with a change in meaning.\n• -ing only: enjoy, avoid, deny, suggest, mind, practise\n• to-inf only: want, hope, decide, refuse, manage, afford"},
            {"type": "concept", "order": 2, "title": "Verbs with Both Forms (Different Meaning)",
             "explanation": "• remember doing = recall a past action (I remember meeting her)\n• remember to do = not forget to do (Remember to lock the door)\n• stop doing = cease an activity\n• stop to do = pause in order to do something\n• try doing = experiment / try to do = make an effort"},
            {"type": "concept", "order": 3, "title": "Verbs with Both Forms (Same Meaning)",
             "explanation": "Some verbs can take either form with little or no change in meaning:\n• begin/start doing/to do\n• continue doing/to do\n• love/hate/like/prefer doing/to do (slight formality difference)"},
            {"type": "concept", "order": 4, "title": "Complex Patterns",
             "explanation": "• verb + object + to-infinitive: I want you to help me.\n• verb + object + infinitive (without to): Let me go. / Make him stop.\n• verb + object + -ing: I saw her crossing the road.\n• verb + preposition + -ing: I look forward to hearing from you."},
            {"type": "advanced", "order": 5, "title": "Advanced Gerund/Infinitive Patterns",
             "explanation": "• It's no use/good crying over spilt milk.\n• There's no point (in) arguing.\n• I can't help laughing. (= I can't stop myself)\n• He went on to become a famous actor. (= next action)\n• He went on talking for hours. (= continued)"}
        ]

    # -----------------------
    # VOCABULARY: Relationships & People (Unit 24)
    # -----------------------
    if topic == "relationships":
        return [
            {"type": "vocabulary", "order": 1, "title": "Topic Vocabulary",
             "explanation": "Key terms: acquaintance, colleague, companion, rival, ally, bond, affection, betrayal, loyalty, commitment, compromise, reconciliation."},
            {"type": "vocabulary", "order": 2, "title": "Phrasal Verbs",
             "explanation": "• get on with = have a good relationship\n• fall out with = argue and stop being friends\n• make up = reconcile after an argument\n• look after = care for\n• bring up = raise (a child)\n• grow apart = gradually become less close"},
            {"type": "vocabulary", "order": 3, "title": "Collocations",
             "explanation": "• close/distant relationship\n• form a friendship / develop a bond\n• have an argument / hold a grudge\n• make amends / break someone's trust\n• unconditional love / mutual respect"},
            {"type": "vocabulary", "order": 4, "title": "Idioms",
             "explanation": "• get off on the wrong foot = bad first impression\n• see eye to eye = agree completely\n• give someone the cold shoulder = ignore\n• have a heart of gold = very kind\n• be two-faced = be insincere"},
            {"type": "vocabulary", "order": 5, "title": "Word Formation",
             "explanation": "• relate → relation → relationship → relative → unrelated\n• friend → friendship → friendly → unfriendly → befriend\n• trust → trustworthy → distrust → mistrust → entrust\n• loyal → loyalty → disloyal → disloyalty"}
        ]

    # -----------------------
    # GRAMMAR: Reporting (Unit 25)
    # -----------------------
    if topic == "reporting":
        return [
            {"type": "intro", "order": 1, "title": "Reported Speech Basics",
             "explanation": "When reporting what someone said, we typically shift tenses back:\n• 'I am tired' → She said she was tired.\n• 'I will come' → He said he would come.\n• 'I have finished' → She said she had finished."},
            {"type": "concept", "order": 2, "title": "Reporting Verbs",
             "explanation": "Different patterns:\n• verb + that: admit, claim, deny, insist, suggest\n• verb + to-inf: agree, offer, promise, refuse, threaten\n• verb + object + to-inf: advise, encourage, remind, warn\n• verb + -ing: deny, recommend, suggest, admit"},
            {"type": "concept", "order": 3, "title": "Reporting Questions & Commands",
             "explanation": "Questions: She asked if/whether I was coming. (yes/no)\nShe asked what time it started. (wh-)\n\nCommands: He told me to sit down.\nHe ordered them not to move.\nShe begged him to help her."},
            {"type": "concept", "order": 4, "title": "Advanced Reporting Patterns",
             "explanation": "• Impersonal: It was reported that / He is said to...\n• Mixed reports: She denied having stolen the money.\n• Reporting with should: He suggested that we (should) leave.\n• Reporting with subjunctive: They demanded that he resign."},
            {"type": "advanced", "order": 5, "title": "Reporting Verbs Nuances",
             "explanation": "Choosing the right verb changes the tone:\n• He said → neutral\n• He insisted → emphatic\n• He admitted → confession\n• He denied → rejection\n• He hinted → indirect\n• He boasted → showing off"}
        ]

    # -----------------------
    # VOCABULARY: Preference & Leisure (Unit 26)
    # -----------------------
    if topic == "leisure":
        return [
            {"type": "vocabulary", "order": 1, "title": "Topic Vocabulary",
             "explanation": "Key terms: pastime, recreation, amateur, enthusiast, spectator, tournament, contestant, competitor, championship, pursuit, thrill-seeker, adrenaline."},
            {"type": "vocabulary", "order": 2, "title": "Phrasal Verbs",
             "explanation": "• take up = start a new hobby\n• give up = stop doing something\n• join in = participate\n• work out = exercise\n• wind down = relax after effort\n• hang out = spend time casually"},
            {"type": "vocabulary", "order": 3, "title": "Collocations",
             "explanation": "• pursue a hobby / take up an interest\n• keen on / fond of / passionate about\n• in your spare time / in your free time\n• a change of scenery\n• do extreme sports / go hiking"},
            {"type": "vocabulary", "order": 4, "title": "Idioms",
             "explanation": "• be a couch potato = very lazy/inactive\n• let your hair down = relax and have fun\n• have the time of your life = enjoy enormously\n• be up for it = be willing/enthusiastic\n• recharge your batteries = rest to regain energy"},
            {"type": "vocabulary", "order": 5, "title": "Word Formation",
             "explanation": "• compete → competition → competitive → competitor → uncompetitive\n• entertain → entertainment → entertaining → entertainer\n• prefer → preference → preferable → preferably\n• enjoy → enjoyment → enjoyable → unenjoyable"}
        ]

    # -----------------------
    # DEFAULT (fallback)
    # -----------------------
    return [
        {"type": "intro", "order": 1, "title": topic.title(),
         "explanation": f"This lesson introduces the topic of {topic}."},
        {"type": "concept", "order": 2, "title": "Core Concepts",
         "explanation": f"In this lesson, you will learn the key ideas related to {topic}."}
    ]

def run_seed():
    db = SessionLocal()

    # 1. Limpiar datos previos
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
        lesson = Lesson(
            title=unit["title"],
            topic=unit["topic"],
            level=lesson_level,
            order=unit["unit"]
        )
        db.add(lesson)
        db.flush()

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