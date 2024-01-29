# RAG Responder

**Description**: RAG Responder is a tool that utilizes Retrieval-Augmented Generation (RAG) techniques to answer questions related to a document. Currently, it supports documents with .txt file extensions. This repository provides a step-by-step guide on how to set up and use the RAG Responder.

## How to Use RAG Responder

Follow these steps to set up and use RAG Responder:

1. **Clone the Repository**:
```bash
    git clone https://github.com/FirasBaba/rag-responder
```
2. **Navigate to the Repository**:
```bash
    cd rag-responder
```
3. **Build the Docker Images**:
```bash
    make build
```
4. **Configure the RAG Responder**:
Open the src/config.py file and select the configuration you would like to use.
5. **Add Your Text Document**:
Copy your text document (in .txt format) to the data/books directory. Make sure to modify the book_name value in src/config.py. The book_name should not include the file extension.
6. **Generate Chunks and Store Embeddings**:
Run the following command to generate chunks from the text document and store the embeddings in a vector database:
```bash
    make run-reader
```
7. **Select the Language Model (LLM)**:
Define the Language Model (LLM) you would like to use via an environment variable. You can choose any model from the Ollama library. For example:
```bash
    export OLLAMA_MODEL_NAME=mistral
```
Feel free to use other LLMs by changing the value of `OLLAMA_MODEL_NAME`.
8. **Start the Ollama Server**:
Run the following command to start the Ollama server. This command will download the model weights, which might take some time depending on your internet connection. Once downloaded, the model will be cached, and you won't need to download it again.
```bash
    make run-ollama
```
9. **Start the Question/Answer System**:
Open a new terminal and define the Language Model (LLM) again via an environment variable, just like in step 7. Then, start the question/answer system with the following commands:
```bash
    export OLLAMA_MODEL_NAME=mistral
    make run-chat
```
10. **Interact with the Question/Answer System**:
You can now interact with the question/answer system in your terminal. Ask any questions you have about the document, and RAG Responder will provide answers based on the content of the document.

## Notes:
- Make sure you have Docker installed to use RAG Responder.
- Feel free to experiment with different Language Models (LLMs) from the Ollama library to see which one works best for your document-related questions.

Enjoy using RAG Responder to quickly get answers from your text documents!