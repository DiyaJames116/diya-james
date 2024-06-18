def retrieve_similar_documents(query_embedding, index, k=5):
    D, I = index.search(query_embedding, k)
    return I

def generate_response(retrieved_docs, query):
    context = " ".join(retrieved_docs)
    response = f"Based on the content: {context} and your query: {query}, here's a generated response."
    return response
