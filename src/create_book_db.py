
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
import os

import config
import utils

import warnings
warnings.filterwarnings("ignore")

documents = utils.load_docs(config.book_name, config.books_directory)
docs = utils.split_docs(documents)
embeder = SentenceTransformerEmbeddings(model_name=config.embedder_name)


db = Chroma.from_documents(docs, embeder)
persist_directory = os.path.join(config.db_dictory, config.book_name)
vectordb = Chroma.from_documents(
    documents=docs, embedding=embeder, persist_directory=persist_directory
)
vectordb.persist()