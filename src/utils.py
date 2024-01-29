from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import config

def load_docs(file_name, directory):
  loader = TextLoader(os.path.join(directory, f"{file_name}.txt"))
  documents = loader.load()
  return documents

def split_docs(documents, chunk_size=config.chunk_size, chunk_overlap=config.chunk_overlap):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs