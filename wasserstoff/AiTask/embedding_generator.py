from sentence_transformers import SentenceTransformer

MODEL_NAME = 'paraphrase-MiniLM-L6-v2'
model = SentenceTransformer(MODEL_NAME)

def generate_embeddings(texts):
    embeddings = model.encode(texts, convert_to_tensor=True)
    return embeddings
