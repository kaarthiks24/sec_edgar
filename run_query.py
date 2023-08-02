from load_agent import load_agents
from tools import create_tools
tools = create_tools()
agent=load_agents(tools)
while True:   
    query = input("\nEnter a query: ")
    # agent({"input":f"{query}"})
    agent.run(query)
    if query == "exit":
        break