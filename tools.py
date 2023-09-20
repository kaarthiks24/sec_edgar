from constants import SOURCE_DIRECTORY, PERSIST_DIRECTORY
import os
from langchain.chains import RetrievalQA
from pydantic import BaseModel, Field
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.agents import Tool
from langchain.prompts import PromptTemplate

'''
Prompt template is defined here
'''
prompt_template = """Your name is Bob and you are a human not an AI assistant. These are risk factors section of SEC 10-K annual filings by companies. Sometimes referred as 10-K SEC filings. If they ask about SEC or 10-K filings it is reffered to the risk factor section what we have. Use the following risk factor sections of 10-K filings from various company filings to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {question}
Helpful Answer:"""



'''
We use the user defined prompt template and pass it to the chain type kwargs
'''
PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)
chain_type_kwargs = {"prompt": PROMPT}



'''
Defining a user defined class for the Document comparison agent
'''
class DocumentInput(BaseModel):
    question: str = Field()




'''
A function which does retreval and create tools for each retriever 
using Langchain
'''
def create_tools():
    files=os.listdir(SOURCE_DIRECTORY)
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
    # creating a tools list to be appended 
    tools=[]
    
    # defining the embeddings
    embeddings = OpenAIEmbeddings()
    
    # iterating through each file for retrieval
    for file in files:
        print(file)
        file_name=file.split('.')[0]
        print(file_name)
        db=Chroma(persist_directory=f"{PERSIST_DIRECTORY}/{file}", embedding_function=embeddings)
        retrievers=db.as_retriever()
        
        # appending tools for each retrieval
        tools.append(
                Tool(
                    args_schema=DocumentInput,
                    name=file_name,
                    description=f"useful when you want to answer questions about {file_name}",
                    func=RetrievalQA.from_chain_type(llm=llm, retriever=retrievers, chain_type_kwargs=chain_type_kwargs),
                )
            )

    return tools
