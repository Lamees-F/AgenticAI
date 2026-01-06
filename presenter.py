from schemas import ClarifiedIdea


def present_clarified_idea(idea: ClarifiedIdea):
    return {
        "Idea Summary": idea.one_liner,
        "Problem": idea.problem_statement,
        "Solution": idea.solution,
        "Target Customer": idea.target_customer,
        "Value Proposition": idea.value_proposition,
        "Key Assumptions": idea.assumptions
    }
