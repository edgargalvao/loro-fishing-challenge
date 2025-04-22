from sklearn.neighbors import NearestNeighbors  # Importa o modelo de vizinhos mais próximos da scikit-learn

# Classe responsável por buscar os textos mais semelhantes a uma pergunta (embedding da pergunta)
class Retriever:
    def __init__(self, embeddings, texts, top_k):
        self.embeddings = embeddings        # Vetores de embedding dos documentos (produtos com specs)
        self.texts = texts                  # Textos correspondentes a cada embedding
        self.model = NearestNeighbors(n_neighbors=top_k, metric='cosine')  # Inicializa o modelo de busca com métrica de similaridade cosseno
        self.model.fit(embeddings)          # Treina o modelo com os embeddings dos documentos

    # Função que recebe um embedding (pergunta) e retorna os textos mais próximos (semelhantes)
    def query(self, embedding):
        distances, indices = self.model.kneighbors([embedding])  # Busca os vizinhos mais próximos do embedding
        return [self.texts[i] for i in indices[0]]               # Retorna os textos correspondentes aos índices encontrados
