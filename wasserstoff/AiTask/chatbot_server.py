from flask import Flask, request, jsonify
import numpy as np
from threading import Thread
import time

from data_retrieval import fetch_wordpress_content
from embedding_generator import generate_embeddings, model
from faiss_index import create_faiss_index
from rag_processor import retrieve_similar_documents
from cot_module import chain_of_thought_response

app = Flask(__name__)
index = None
texts = []

EMBEDDING_REFRESH_INTERVAL = 3600  # in seconds

def update_faiss_index():
    global index, texts
    content = fetch_wordpress_content()
    
    if content:
        print(f"Fetched content type: {type(content)}")
        print(f"Fetched content: {content}")

        if isinstance(content, dict) and 'posts' in content:
            posts = content['posts']
            
            if isinstance(posts, list):
                texts = [post['content']['rendered'] for post in posts if 'content' in post and 'rendered' in post['content']]
                print(f"Extracted texts: {texts}")

                if texts:
                    embeddings = generate_embeddings(texts)
                    embedding_list = [embedding.numpy() for embedding in embeddings]
                    embedding_array = np.vstack(embedding_list)
                    index = create_faiss_index(embedding_array)
                    print("Faiss index updated with new embeddings.")
                else:
                    print("No valid texts found in posts.")
            else:
                print("The 'posts' key does not contain a list.")
        else:
            print("Fetched content does not contain 'posts' or is not a dictionary.")
    else:
        print("Failed to fetch valid content from WordPress.")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    query = data['query']
    query_embedding = model.encode([query], convert_to_tensor=True).numpy()
    retrieved_indices = retrieve_similar_documents(query_embedding, index)
    retrieved_docs = [texts[i] for i in retrieved_indices[0]]
    response = chain_of_thought_response(retrieved_docs, query)
    return jsonify({'response': response})

def periodic_index_update():
    while True:
        update_faiss_index()
        time.sleep(EMBEDDING_REFRESH_INTERVAL)

if __name__ == '__main__':
    thread = Thread(target=periodic_index_update)
    thread.start()
    app.run(port=5000)
