
import json 

from utils.openAI_client import ask_openai

from agents.summary_agent import SummarizerAgent
from agents.concept_agent import ConceptAgent
from agents.quiz_agent import QuizAgent
from agents.learning_coach_agent import LearningCoachAgent

class PlannerAgent:
    def decide_agents(self, user_request):
        prompt = f"""
        Your only job is to decide which specialist agents should run.

        Available agents:

        - summarizer: summarizes notes
        - concept: extracts important concepts and definitions
        - quiz: generates quiz questions directly from the notes
        - coach: gives study advice

        Rules:

        1. If the user only asks for a summary:
        select only "summarizer".

        2. If the user only asks for concepts or definitions:
        select only "concept".

        3. If the user only asks for quiz questions:
        select only "quiz".

        4. If the user only asks for study advice:
        select only "coach".

        5. If the user asks for full exam preparation:
        select all four agents.

        6. Do not select extra agents that the user did not request.

        7. If the user gives a number of quiz questions, extract that number.
        Otherwise use 5.

        User request:
        {user_request}

        Return valid JSON only in this format:

        {{
        "selected_agents": ["quiz"],
        "quiz_count": 10,
        "reason": "The user requested only 10 quiz questions."
        }}
        """

        response_text = ask_openai(prompt)

        try:
            return json.loads(response_text)
        except json.JSONDecodeError:
            return {
                "selected_agents": ["summarizer", "concept", "quiz", "coach"],
                "reason": "Planner response was not valid JSON, so all agents were selected."
            }

    def run(self, notes: str, user_request: str) -> dict:
        plan = self.decide_agents(user_request)

        selected = plan.get("selected_agents", [])

        result = {
            "planner_reason": plan.get("reason", ""),
            "selected_agents": selected
        }

        if "summarizer" in selected:
            result["summary"] = SummarizerAgent().run(notes)

        if "concept" in selected:
            result["concepts"] = ConceptAgent().run(notes)

        if "quiz" in selected:
            result["quiz"] = QuizAgent().run(
                notes=notes,
                question_count=plan.get("quiz_count", 5)
            )

        if "coach" in selected:
            result["coach"] = LearningCoachAgent().run(
                notes=notes,
                summary=result.get("summary", ""),
                concepts=result.get("concepts", ""),
                quiz=result.get("quiz", "")
            )

        return result