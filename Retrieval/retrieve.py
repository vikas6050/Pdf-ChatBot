from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI, OpenAIEmbeddings

import os
from typing import Any, Dict, List
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores.pinecone import Pinecone as PineconeLangChain
import pinecone 


pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV_NAME")
)


INDEX_NAME = "langchan-docs"


def run_llm(query: str, chat_history: List[Dict[str, Any]] = []):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    docsearch = PineconeLangChain.from_existing_index(
        embedding=embeddings,
        index_name=INDEX_NAME,
    )
    chat = ChatOpenAI(
        verbose=True,
        temperature=0.5,
    )

    qa = ConversationalRetrievalChain.from_llm(
        llm=chat, retriever=docsearch.as_retriever(), return_source_documents=True
    )
    return qa.invoke({"question": query, "chat_history": chat_history})

if __name__ == "__main__":
    print(run_llm(query = "What is a record deal?"))