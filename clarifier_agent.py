from pydantic import BaseModel, Field
from agents import Agent
import os
from dotenv import load_dotenv
load_dotenv(override=True)

MODEL_NAME = os.getenv("DEFAULT_MODEL_NAME", "gpt-5.4-mini")

INSTRUCTIONS = """
You are a research assistant. Given a user's research query, ask exactly 3
clarifying questions that would help you produce a more targeted, useful report.
The questions must be specific to this query — think about what's ambiguous,
what scope/angle/timeframe/depth is unclear, and what would change how you'd research it.
Do not ask generic questions unrelated to this specific topic.
"""


class ClarificationQuestions(BaseModel):
    questions: list[str] = Field(description="Exactly 3 clarifying questions specific to the user's query.")


clarifier_agent = Agent(name="Clarifier Agent", instructions=INSTRUCTIONS, model=MODEL_NAME, output_type=ClarificationQuestions)
