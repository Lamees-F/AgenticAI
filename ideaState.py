from schemas import ClarifiedIdea


class IdeaState:
    def __init__(self, original_input: str):
        self.original_input = original_input
        self.versions: list[ClarifiedIdea] = []

    def add_version(self, idea: ClarifiedIdea):
        self.versions.append(idea)

    def latest(self) -> ClarifiedIdea:
        return self.versions[-1]
