import os
import requests
import json
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
import joblib

import config
import warnings
warnings.filterwarnings("ignore")

embedder_path = f"../data/embeddings/{config.embedder_name}"
if os.path.exists(embedder_path):
    embeddings = joblib.load(embedder_path)
else:
    embeddings = SentenceTransformerEmbeddings(model_name=config.embedder_name)
    directory_path = "../data/embeddings"
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    joblib.dump(embeddings, embedder_path)

db = Chroma(persist_directory=f"{config.db_dictory}/{config.book_name}", embedding_function=embeddings)
try:
    while True:
        query = input("Enter your query: ")
        matching_docs = db.similarity_search(query, )

        docs = [msg.page_content for msg in matching_docs]

        prompt = f"<<SYS>> You are a Retrieval Augmented Generation chatbot. Answer user queries using only the provided context while respecting the rules below. If the context does not provide enough information, say so. If the answer requires code examples encapsulate them with ```programming-language-name ```. Don't do pseudo-code. \n"\
        + "Rule 1: Your answer needs to be only inspired from the paragraphs.\n"\
        + "Rule 2: Your answer needs to have a meaning.\n"\
        + "Rule 3: If the content does not have an answer, do not answer with your general knowledge.\n"\
        + "Rule 4: Do not mention that you are an AI model. Always try to look like a human being.\n"\
        + "Rule 5: you name is RojlaMax. <</SYS>>\n"\
        + f"Answer this query: {query}\n"\
        + "\n".join([f"This is the context {i+1}: {doc}" for i, doc in enumerate(docs)])

        url = "http://ollama-service:11434/api/generate"

        headers = {
            "Content-Type": "application/json"
        }
        if os.getenv("OLLAMA_MODEL_NAME"):
            data = {
                "model": os.getenv("OLLAMA_MODEL_NAME"),
                "prompt": prompt,
                "stream": False
            }
        else:
            model_name = input("Please set the OLLAMA_MODEL_NAME environment variable to the desired model name:")
            os.environ["OLLAMA_MODEL_NAME"] = model_name
            data = {
                "model": os.getenv("OLLAMA_MODEL_NAME"),
                "prompt": prompt,
                "stream": False
            }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(response)
        response = json.loads(response.text)
        print(response["response"])

except KeyboardInterrupt:
    print("CTRL + C pressed. Exiting...")