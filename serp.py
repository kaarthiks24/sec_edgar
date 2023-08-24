import os
import pprint

os.environ["SERPER_API_KEY"] = "6214b92b136edb4c88df671cba1fa3e745c604a8"
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.llms.openai import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

llm = OpenAI(temperature=0)
search = GoogleSerperAPIWrapper()
tools = [
    Tool(
        name="Intermediate Answer",
        func=search.run,
        description="useful for when you need to ask with search",
    )
]

self_ask_with_search = initialize_agent(
    tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True
)

while True:
    query=input("Enter query:")
    if query:
        self_ask_with_search.run(query)
    elif query=="exit":
        break
