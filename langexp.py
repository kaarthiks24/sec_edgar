from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough

from load_agent import load_agents
from tools import create_tools

from langchain.chat_models import ChatOpenAI
tools = create_tools()
agent=load_agents(tools)
from langchain.schema.output_parser import StrOutputParser
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
model=ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo-0613",
    )
chain = (
    {"context": tools, "question": RunnablePassthrough()} 
    | prompt 
    | model 
    | StrOutputParser()
)