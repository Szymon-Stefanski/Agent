from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
response = llm.invoke("What is a Bydgoszcz?")
print(response)
