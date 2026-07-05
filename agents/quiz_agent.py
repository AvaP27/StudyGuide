from utils.openAI_client import ask_openai
class QuizAgent:
    def run(self, summary, concepts):
        prompt = f"""
        You are a quiz generation agent.

        Create 10 multiple-choice questions.

        Include:
        - Question
        - Four answer choices
        - Correct answer
        - Short explanation

        Summary:
        {summary}

        Concepts:
        {concepts}
        """
        return ask_openai(prompt)