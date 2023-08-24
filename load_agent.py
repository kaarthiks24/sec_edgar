import langchain
from langchain.agents import AgentType, initialize_agent
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
import os
import openai
from langchain_plantuml import plantuml, diagram
from langchain.prompts import PromptTemplate
from tools import PROMPT

def load_agents(tools):
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo-0613",
    )
    
    langchain.debug=True
    
    agent = initialize_agent(
        agent=AgentType.OPENAI_FUNCTIONS,
        tools=tools,
        llm=llm,
        verbose=True,
    )
    
    return agent