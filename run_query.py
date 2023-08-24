from load_agent import load_agents
from tools import create_tools
from langchain_plantuml import plantuml, diagram
import langchain_visualizer
from langchain_visualizer import visualize_embeddings
import asyncio
callback_handler = diagram.activity_diagram_callback()
tools = create_tools()
agent=load_agents(tools)
async def search_agent_demo():
    query = input("\nEnter a query: ")
    return agent.run(input("Enter a question:"))


langchain_visualizer.visualize(search_agent_demo)
