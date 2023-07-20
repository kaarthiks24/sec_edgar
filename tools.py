from constants import SOURCE_DIRECTORY, PERSIST_DIRECTORY
import os
from langchain.chains import RetrievalQA
from pydantic import BaseModel, Field
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.agents import Tool

class DocumentInput(BaseModel):
    question: str = Field()
    
def create_tools():
    files=os.listdir(SOURCE_DIRECTORY)
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
    tools=[]
    embeddings = OpenAIEmbeddings()
    for file in files:
        print(file)
        file_name=file.split('.')[0]
        print(file_name)
        db=Chroma(persist_directory=f"{PERSIST_DIRECTORY}/{file}", embedding_function=embeddings)
        retrievers=db.as_retriever()
        tools.append(
                Tool(
                    args_schema=DocumentInput,
                    name=file_name,
                    description=f"useful when you want to answer questions about {file_name}",
                    func=RetrievalQA.from_chain_type(llm=llm, retriever=retrievers),
                )
            )
    return tools
