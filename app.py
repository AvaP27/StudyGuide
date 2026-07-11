import streamlit as st
from planner_agent import PlannerAgent

st.set_page_config(page_title="StudyGuide", page_icon="🎓")

st.title("🎓 StudyGuide")
st.write("A multi-agent study assistant using OpenAI.")

notes = st.text_area("Paste your class notes here:", height=250)

user_request = st.text_input(
    "What do you want help with?",
    placeholder="Example: I have an exam tomorrow. Help me prepare."
)

if st.button("Generate Notes"):
    if not notes.strip():
        st.warning("Please paste some notes first.")
    elif not user_request.strip():
        st.warning("Please enter what you want help with.")
    else:
        with st.spinner("Planner agent is deciding what to do..."):
            planner = PlannerAgent()
            result = planner.run(notes=notes, user_request=user_request)

        st.subheader("Planner Decision")
        st.write(result.get("planner_reason", ""))

        if "summary" in result:
            st.subheader("Summary")
            st.write(result["summary"])

        if "concepts" in result:
            st.subheader("Key Concepts")
            st.write(result["concepts"])

        if "quiz" in result:
            st.subheader("Quiz")
            st.write(result["quiz"])

        if "coach" in result:
            st.subheader("Learning Coach")
            st.write(result["coach"])