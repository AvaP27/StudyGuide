from utils.openAI_client import ask_openai
class SummarizerAgent:
    def run(self, notes):
        prompt = f"""
        You are a study assistant.

        Summarize these notes in simple English.

        Include:
        - Main idea
        - Key points
        - Important facts

        Notes:
        {notes}
        """
        return ask_openai(prompt)