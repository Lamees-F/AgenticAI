from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import GalaxonOrchestrator

app = FastAPI()
orchestrator = GalaxonOrchestrator()


class IdeaInput(BaseModel):
    idea: str


@app.post("/analyze")
def analyze(input: IdeaInput):
    return orchestrator.run(input.idea)
