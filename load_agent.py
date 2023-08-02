import langchain
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
import os
import openai
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo,
)
from langchain.llms import OpenLLM
from langchain.memory import ConversationBufferMemory


def load_agents(tools):
    # llm = ChatOpenAI(
    #     temperature=0,
    #     model="gpt-3.5-turbo-0613",
    # )
    memory = ConversationBufferMemory(memory_key="chat_history")
    llm= OpenLLM(model_name="falcon", model_id='tiiuae/falcon-7b-instruct', device_map='auto')

    langchain.debug = True
    agent= initialize_agent(tools, llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)

    # agent = initialize_agent(
    #     agent=AgentType.OPENAI_FUNCTIONS,
    #     tools=tools,
    #     llm=llm,
    #     verbose=True,
    # )
    return agent