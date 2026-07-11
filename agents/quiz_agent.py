from utils.openAI_client import ask_openai

class QuizAgent:
    def run(self, notes: str, question_count: int = 5) -> str:
        prompt = f"""
You are a quiz generation agent.

Create exactly {question_count} multiple-choice questions using only the
student notes below.

For every question include:

- Question
- Four options labeled A, B, C, and D
- Correct answer
- Short explanation

Rules:

- Create exactly {question_count} questions.
- Use only information from the notes.
- Do not add outside facts.
- Test understanding, not only memorization.
- Avoid repeated questions.
- Use clear language suitable for a student.

Student notes:

{notes}
"""

        return ask_openai(prompt)