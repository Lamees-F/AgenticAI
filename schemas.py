## structured output
from pydantic import BaseModel
from typing import List


class ClarifiedIdea(BaseModel):
    one_liner: str
    problem_statement: str
    solution: str
    target_customer: str
    value_proposition: str
    assumptions: List[str]
