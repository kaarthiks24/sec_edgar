import functools
import os
import logging
from constants import PERSIST_DIRECTORY, SOURCE_DIRECTORY
from langchain.chat_models import ChatOpenAI

from pydantic import BaseModel, Field
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
print(PERSIST_DIRECTORY, SOURCE_DIRECTORY)

import openai


class DocumentInput(BaseModel):
        question: str = Field()

def create_DB():
    tools = []

    logging.info(f"Loading documents from {SOURCE_DIRECTORY}")
    files=os.listdir(SOURCE_DIRECTORY)
    print(files)
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
    for file in files:
        # print(file)
        file_name=file.split('.')[0]
        print(file_name)
        file_path = os.path.join(SOURCE_DIRECTORY, file)
        print("File path: ",file_path)
        loader = TextLoader(file_path)
        # file=loader.load()
        # print("____Before metadata addition:____", file)
        # for doc in file:
        #     # print("Before:",doc.metadata)
        #     doc.metadata['Document type:']="10-K filings"
        #     doc.metadata['Filing section']="Risk factors"
            # print("After:",doc.metadata)
        # print("_____After metadata addition___",file)
        pages = loader.load_and_split()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(pages)
        embeddings = OpenAIEmbeddings()
        db = Chroma.from_documents(docs,embeddings,persist_directory=f"{PERSIST_DIRECTORY}/{file}")
        # db.persist()
        retrievers= db.as_retriever()
        # db=Chroma.from_documents(docs, embeddings)
        # retrievers=db.as_retriever()
        file_name=file.split('.')[0]
        
    return ""


def main():
    create_DB()


if __name__ == "__main__":
    main()