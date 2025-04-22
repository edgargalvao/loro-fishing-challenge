from sklearn.neighbors import NearestNeighbors

class Retriever:
    def __init__(self, embeddings, texts, top_k):
        self.embeddings = embeddings
        self.texts = texts
        self.model = NearestNeighbors(n_neighbors=top_k, metric='cosine')
        self.model.fit(embeddings)

    def query(self, embedding):
        distances, indices = self.model.kneighbors([embedding])
        return [self.texts[i] for i in indices[0]]
