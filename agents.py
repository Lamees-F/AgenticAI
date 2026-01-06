from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from baseAgent import BaseAgent
from schemas import ClarifiedIdea


# ---------- CLARIFIER (STRUCTURED) ----------

clarifier_parser = PydanticOutputParser(
    pydantic_object=ClarifiedIdea
)

clarifier_prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are a startup advisor and product strategist.

Your task:
- Clarify vague business ideas
- Identify the real problem
- Define a clear solution and target customer
- Remove buzzwords and ambiguity

Rules:
- Be concrete and realistic
- Avoid hype
- Do NOT invent data

Return STRICT JSON only.
"""),
    ("human", """
Business idea:
{idea}

{format_instructions}
""")
])

clarifier_llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2
)

clarifier_chain = clarifier_prompt | clarifier_llm | clarifier_parser


def run_clarifier(idea: str) -> ClarifiedIdea:
    return clarifier_chain.invoke({
        "idea": idea,
        "format_instructions": clarifier_parser.get_format_instructions()
    })


# ---------- OTHER AGENTS (TEXT) ----------

industry_agent = BaseAgent("""
You are a market analyst.

Identify:
- Primary industry
- Adjacent industries
- Key market forces
""")

competitor_agent = BaseAgent("""
You are a competitive intelligence analyst.

Identify competitors and group them into archetypes.
Avoid hallucinations.
""")

opportunity_agent = BaseAgent("""
You are a venture analyst.

Identify market gaps and opportunity zones.
Focus on unmet needs.
""")

blindspot_agent = BaseAgent("""
You are a critical reviewer.

Identify missing elements and risky assumptions.
Be skeptical and precise.
""")
