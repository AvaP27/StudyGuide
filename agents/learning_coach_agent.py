from utils.openAI_client import ask_openai
class LearningCoachAgent:
    def run(self, summary, concepts, quiz):
        prompt = f"""
        You are a learning coach.

        Give simple study advice based on the summary, concepts, and quiz.

        Include:
        - What to review first
        - Weak areas to watch
        - 3 study tips

        Summary:
        {summary}

        Concepts:
        {concepts}

        Quiz:
        {quiz}
        """
        return ask_openai(prompt)


