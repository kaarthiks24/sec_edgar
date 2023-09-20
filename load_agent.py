import langchain
from langchain.agents import AgentType, initialize_agent
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
import os
import openai
# from langchain_plantuml import plantuml, diagram
from langchain.prompts import PromptTemplate
from tools import PROMPT

'''
Using the langchain agents
'''
def load_agents(tools):
    
    # Defining the llm to be used 
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo-0613",
    )
    
    '''
    True: Run the program in debug mode
    False: Run the program in normal mode
    '''
    langchain.debug=True
    
    agent = initialize_agent(
        agent=AgentType.OPENAI_FUNCTIONS,
        tools=tools,
        llm=llm,
        verbose=True,
    )
    
    return agent