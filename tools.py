from langchain_community.tools import WikipediaQueryRun
from langchain_google_community import GoogleSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

search = GoogleSearchRun
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information",
)
