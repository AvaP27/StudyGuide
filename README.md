StudyGuide 

About the Project

StudyPilot AI is a study helper application that I built using Python, Streamlit, and the OpenAI API.

The purpose of this project is to help students study better. The application can summarize notes, find important concepts, create quiz questions, and give study suggestions.

Instead of using only one AI prompt, this project uses multiple AI agents. A Planner Agent first understands what the student wants and then decides which agents should work on the task.

Features

Summarize study notes

Find important concepts

Generate quiz questions

Give study tips

Use a Planner Agent to choose the right AI agents

Simple and easy-to-use web interface

Project Architecture

Student
    │
    ▼
Streamlit App
    │
    ▼
Planner Agent
    │
 ┌─────────────┬──────────────┬──────────────┐
 │             │              │              │
 ▼             ▼              ▼              ▼
Summarizer  Concept Agent  Quiz Agent  Learning Coach
                     │
                     ▼
                 OpenAI API
Technologies Used

Python

Streamlit

OpenAI API

python-dotenv

Git

GitHub

Project Structure

StudyPilot-AI/

app.py
planner_agent.py

agents/
    summarizer_agent.py
    concept_agent.py
    quiz_agent.py
    learning_coach_agent.py

utils/
    openai_client.py

requirements.txt
README.md
How It Works

The student enters notes and a question.

The Planner Agent understands the request.

It decides which AI agents should be used.

Each agent completes its own task.

The results are shown in the Streamlit application.

How to Run

Clone the repository:

git clone <repository-url>
Create a virtual environment:

python -m venv .venv
Activate the virtual environment (Windows):

.\.venv\Scripts\Activate.ps1
Install the required packages:

pip install -r requirements.txt
Create a .env file and add your OpenAI API key:

OPENAI_API_KEY=your_api_key
Run the application:

streamlit run app.py
Open your browser and go to:

http://localhost:8501
Future Improvements

Upload PDF notes

Save study history

Better quiz questions

Progress tracking

Flashcards

Support for more AI models

What I Learned

While working on this project, I learned:

Python programming

OpenAI API

Prompt engineering

AI agents

Streamlit

Git and GitHub

How AI applications are built

Note

This project was created as a learning project to understand AI agents and modern AI application development.