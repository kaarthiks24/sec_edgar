from constants import SOURCE_DIRECTORY, PERSIST_DIRECTORY
import os
from langchain.chains import RetrievalQA
from pydantic import BaseModel, Field
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.agents import Tool, load_tools
from langchain import LLMMathChain
from langchain.prompts import PromptTemplate

prompt_template = """These are risk factors section of SEC 10-K annual filings by companies. Sometimes referred as 10-K SEC filings. If they ask about SEC or 10-K filings it is reffered to the risk factor section what we have. Use the following risk factor sections of 10-K filings from various company filings to answer the question at the end. If any math related questions asked use the MathChain. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {question}
Helpful Answer:"""
PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)
chain_type_kwargs = {"prompt": PROMPT}
class DocumentInput(BaseModel):
    question: str = Field()

class MathChain(BaseModel):
    question: int=Field()
    
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
                    func=RetrievalQA.from_chain_type(llm=llm, retriever=retrievers, chain_type_kwargs=chain_type_kwargs),
                )
            )
    # tools.append(Tool(args_schema=MathChain,name="Math tool",description="use this tool when you need to calculate math problems like nultiply, adding", func=LLMMathChain(llm=llm)))
    
    return tools
