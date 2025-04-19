from sklearn.neighbors import NearestNeighbors

class Retriever:
    def __init__(self, embeddings, texts):
        self.embeddings = embeddings
        self.texts = texts
        self.model = NearestNeighbors(n_neighbors=1, metric='cosine')
        self.model.fit(embeddings)

    def query(self, embedding):
        distances, indices = self.model.kneighbors([embedding])
        return self.texts[indices[0][0]]
