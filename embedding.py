import os
from dotenv import load_dotenv
import pinecone 
from langchain_openai import OpenAIEmbeddings
from PyPDF2 import PdfReader
from langchain_community.vectorstores import Pinecone as PineconeLangChain

load_dotenv()

pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV_NAME")
)

INDEX_NAME = "langchan-docs"

class Document:
    def __init__(self, content, metadata):
        self.page_content = content
        self.metadata = metadata

def ingest_docs():
    pdf_reader = PdfReader('Celebrity.pdf')
    texts = []
    for page in pdf_reader.pages:
        chunks = page.extract_text()
        texts.append(chunks)
    
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    print(f"Going to add {len(texts)} documents to Pinecone")
    
    # Create separate documents for each page
    page_documents = [
        Document(content=text, metadata={"page": index}) for index, text in enumerate(texts)
    ]
    
    PineconeLangChain.from_documents(page_documents, embeddings, index_name=INDEX_NAME)
    print("****Loading to vectorstore done ***")

if __name__ == "__main__":
    ingest_docs()
