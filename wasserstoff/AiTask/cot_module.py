from rag_processor import generate_response

def chain_of_thought_response(retrieved_docs, query):
    context = " ".join(retrieved_docs)
    thoughts = []
    current_thought = query
    for _ in range(3):
        current_thought = generate_response(retrieved_docs, current_thought)
        thoughts.append(current_thought)
    return " ".join(thoughts)
