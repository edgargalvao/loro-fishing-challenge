# Importa o modelo de embeddings da biblioteca SentenceTransformers
from sentence_transformers import SentenceTransformer

# Função para carregar o modelo de embedding
def get_model():
    # Retorna o modelo 'all-MiniLM-L6-v2', um modelo leve e eficiente para gerar embeddings de sentenças
    return SentenceTransformer('all-MiniLM-L6-v2')

# Função para gerar embeddings a partir de uma lista de textos
def embed_texts(texts, model):
    # Aplica o modelo para codificar todos os textos em vetores numéricos (embeddings)
    return model.encode(texts)
