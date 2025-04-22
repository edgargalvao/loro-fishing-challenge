from src.data_loader import load_data, merge_data
from src.embedder import get_model, embed_texts
from src.retriever import Retriever

class QASystem:
    def __init__(self, product_path, specs_path):
        self.products, self.specs = load_data(product_path, specs_path)
        self.docs = merge_data(self.products, self.specs)
        self.model = get_model()
        self.embeddings = embed_texts(self.docs, self.model)
        self.retriever = Retriever(self.embeddings, self.docs, top_k = 5)

    def answer(self, question):
        query_embedding = self.model.encode(question)
        return self.retriever.query(query_embedding)
