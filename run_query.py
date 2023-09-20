from load_agent import load_agents
from tools import create_tools

import langchain_visualizer


tools = create_tools()
agent=load_agents(tools)
async def search_agent_demo():
    query = input("\nEnter a query: ")
    return agent.run(input("Enter a question:"))


langchain_visualizer.visualize(search_agent_demo)
