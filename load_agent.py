import langchain
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
import os
import openai


def load_agents(tools):
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo-0613",
    )
    langchain.debug = False
    

    agent = initialize_agent(
        agent=AgentType.OPENAI_MULTI_FUNCTIONS,
        tools=tools,
        llm=llm,
        verbose=True,
    )
    return agent