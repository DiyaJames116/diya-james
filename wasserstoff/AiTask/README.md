# Chatbot with Retrieval-Augmented Generation and Chain of Thought

This project implements a versatile, intelligent chatbot that uses a Retrieval-Augmented Generation (RAG) system enhanced with a Chain of Thought (CoT) strategy. The chatbot integrates with WordPress sites to handle a wide range of topics and maintain logical, contextually relevant interactions.

## File Structure

- `data_retrieval.py`: Handles fetching content from WordPress.
- `embedding_generator.py`: Generates embeddings using Sentence-BERT.
- `faiss_index.py`: Manages the Faiss index for storing and retrieving embeddings.
- `rag_processor.py`: Processes retrieval and generates responses.
- `cot_module.py`: Implements the Chain of Thought logic.
- `chatbot_server.py`: The main server script that integrates all components and runs the Flask app.
- `requirements.txt`: Lists the dependencies required to run the project.
- `README.md`: Provides an overview and instructions for setting up and running the project.

## Setup

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
