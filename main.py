from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import AnthropicPrompts
from langchain_core.output_parsers import PythonOutputParser

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")

