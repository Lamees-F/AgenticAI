import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from orchestrator import GalaxonOrchestrator
from refinementAgent import refine_idea
from ideaState import IdeaState
from presenter import present_clarified_idea

st.set_page_config(
    page_title="Galaxon – AI Startup Advisor",
    layout="wide"
)

st.title("🚀 Galaxon – AI Startup Advisor")
st.caption("Turn a vague idea into a clear, actionable startup concept")

# Initialize orchestrator
orchestrator = GalaxonOrchestrator()

# Session state
if "idea_state" not in st.session_state:
    st.session_state.idea_state = None
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None


# -------- USER INPUT --------
idea_input = st.text_area(
    "Describe your business idea (rough ideas are fine):",
    height=150,
    placeholder="Example: An AI tool to help small businesses grow..."
)

if st.button("Analyze Idea"):
    if idea_input.strip():
        with st.spinner("Analyzing your idea..."):
            result = orchestrator.run(idea_input)
            st.session_state.analysis_result = result
            st.session_state.idea_state = IdeaState(idea_input)

            # Save clarified version to memory
            clarified_obj = result["clarified_idea"]
    else:
        st.warning("Please enter a business idea.")


# -------- DISPLAY RESULTS --------
if st.session_state.analysis_result:

    result = st.session_state.analysis_result

    st.subheader("💡 Clarified Idea")
    st.json(result["clarified_idea"])

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏭 Industry")
        st.write(result["industry"])

    with col2:
        st.subheader("🥊 Competitors")
        st.write(result["competitors"])

    st.subheader("🚀 Opportunity")
    st.write(result["opportunity"])

    st.subheader("⚠️ Blind Spots")
    st.write(result["blind_spots"])


# -------- REFINEMENT LOOP --------
if st.session_state.analysis_result:

    st.divider()
    st.subheader("🔄 Refine Your Idea")

    refinement_feedback = st.text_input(
        "What would you like to refine? (e.g. pricing, niche, customer type)"
    )

    if st.button("Refine Idea"):
        if refinement_feedback.strip():
            with st.spinner("Refining idea..."):
                state = st.session_state.idea_state
                latest = state.latest()

                refined = refine_idea(
                    current_idea=latest,
                    feedback=refinement_feedback
                )

                state.add_version(refined)

                st.subheader("✨ Refined Idea")
                st.json(present_clarified_idea(refined))
        else:
            st.warning("Enter refinement feedback.")
