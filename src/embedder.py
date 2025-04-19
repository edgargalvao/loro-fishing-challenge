from sentence_transformers import SentenceTransformer

def get_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

def embed_texts(texts, model):
    return model.encode(texts)
