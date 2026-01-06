from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from schemas import ClarifiedIdea


parser = PydanticOutputParser(pydantic_object=ClarifiedIdea)

prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are a startup mentor refining an existing idea.

Improve clarity and business viability.
Preserve the core idea.
Avoid feature creep.
"""),
    ("human", """
Current idea:
{current_idea}

User refinement request:
{feedback}

{format_instructions}
""")
])

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
refinement_chain = prompt | llm | parser


def refine_idea(current_idea: ClarifiedIdea, feedback: str) -> ClarifiedIdea:
    return refinement_chain.invoke({
        "current_idea": current_idea.json(),
        "feedback": feedback,
        "format_instructions": parser.get_format_instructions()
    })
