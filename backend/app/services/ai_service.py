import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

# Create client once
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_placement_test():

    prompt = """
Generate a 30-question English placement test from A1 to C1.

Rules:
- Multiple choice
- 4 options per question
- Only ONE correct answer
- Mix grammar and vocabulary
- Difficulty increasing gradually

Return ONLY valid JSON.

Format:

[
 {
   "id":1,
   "question":"...",
   "options":["A","B","C","D"],
   "correct":"..."
 }
]
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
        ),
    )

    # safer extraction
    if response.text:
        content = response.text
    else:
        content = response.candidates[0].content.parts[0].text

    content = content.strip()

    # Remove markdown if Gemini adds it
    if content.startswith("```json"):
        content = content[7:]
    elif content.startswith("```"):
        content = content[3:]

    if content.endswith("```"):
        content = content[:-3]

    content = content.strip()

    try:
        questions = json.loads(content)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON returned by Gemini: {content}") from e

    return questions