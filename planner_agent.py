
import json 

from utils.openAI_client import ask_openai

from agents.summary_agent import SummarizerAgent
from agents.concept_agent import ConceptAgent
from agents.quiz_agent import QuizAgent
from agents.learning_coach_agent import LearningCoachAgent

class PlannerAgent:
    def decide_agents(self, user_request):
        prompt = f"""
        You are a planner agent for a study assistant app.

        Available agents:
        - summarizer
        - concept
        - quiz
        - coach

        User request:
        {user_request}

        Decide which agents are needed.

        Rules:
        - If user wants explanation, use summarizer and concept.
        - If user wants quiz, use summarizer, concept, and quiz.
        - If user has exam/test soon, use all agents.
        - If unsure, use all agents.

        Return JSON only:
        {{
          "selected_agents": ["summarizer", "concept", "quiz", "coach"],
          "reason": "short reason"
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

    def run(self, notes, user_request):
        plan = self.decide_agents(user_request)
        selected_agents = plan["selected_agents"]

        result = {
            "selected_agents": selected_agents,
            "planner_reason": plan.get("reason", "")
        }

        if "summarizer" in selected_agents:
            result["summary"] = SummarizerAgent().run(notes)

        if "concept" in selected_agents:
            concept_input = result.get("summary", notes)
            result["concepts"] = ConceptAgent().run(concept_input)

        if "quiz" in selected_agents:
            result["quiz"] = QuizAgent().run(
                summary=result.get("summary", ""),
                concepts=result.get("concepts", "")
            )

        if "coach" in selected_agents:
            result["coach"] = LearningCoachAgent().run(
                summary=result.get("summary", ""),
                concepts=result.get("concepts", ""),
                quiz=result.get("quiz", "")
            )

        return result