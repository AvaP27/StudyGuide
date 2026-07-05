from utils.openAI_client import ask_openai
class ConceptAgent:
    def run(self, notes_or_summary):
        prompt = f"""
        You are a concept extraction agent.

        Extract the most important concepts.

        For each concept include:
        - Concept name
        - Definition
        - Why it matters

        Text:
        {notes_or_summary}
        """
        return ask_openai(prompt)
