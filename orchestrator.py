from agents import (
    run_clarifier,
    industry_agent,
    competitor_agent,
    opportunity_agent,
    blindspot_agent
)
from ideaState import IdeaState
from presenter import present_clarified_idea


class GalaxonOrchestrator:

    def run(self, user_idea: str):

        state = IdeaState(user_idea)

        clarified = run_clarifier(user_idea)
        state.add_version(clarified)

        industry = industry_agent.run(
            task="Identify industry and market forces.",
            context=clarified.json()
        )

        competitors = competitor_agent.run(
            task="Identify competitors and archetypes.",
            context=clarified.json()
        )

        opportunity = opportunity_agent.run(
            task="Identify opportunity space.",
            context=f"{clarified.json()}\n{industry}"
        )

        blindspots = blindspot_agent.run(
            task="Identify blind spots.",
            context=clarified.json()
        )

        return {
            "clarified_idea": present_clarified_idea(clarified),
            "industry": industry,
            "competitors": competitors,
            "opportunity": opportunity,
            "blind_spots": blindspots
        }
