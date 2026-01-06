from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


class BaseAgent:
    def __init__(self, system_prompt: str):
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "Task:\n{task}\n\nContext:\n{context}")
        ])

        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.3
        )

        self.chain = self.prompt | self.llm

    def run(self, task: str, context: str) -> str:
        response = self.chain.invoke({
            "task": task,
            "context": context
        })
        return response.content
