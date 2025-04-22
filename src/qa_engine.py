# Importa funções utilitárias para carregar e unir os dados dos CSVs
from src.data_loader import load_data, merge_data

# Importa funções para carregar modelo de embeddings e gerar embeddings dos textos
from src.embedder import get_model, embed_texts

# Importa o retriever que vai buscar os textos mais relevantes com base nos embeddings
from src.retriever import Retriever

# Importa a pipeline de Pergunta e Resposta da Hugging Face
from transformers import pipeline

# Define a classe principal do sistema de Pergunta e Resposta
class QASystem:
    def __init__(self, product_path, specs_path, top_k=3):
        # Carrega os dados dos produtos e das especificações técnicas a partir dos CSVs
        self.products, self.specs = load_data(product_path, specs_path)

        # Mescla os dados dos dois CSVs em uma lista única de documentos
        self.docs = merge_data(self.products, self.specs)

        # Carrega o modelo de embeddings (ex: SentenceTransformer)
        self.model = get_model()

        # Gera embeddings para cada documento
        self.embeddings = embed_texts(self.docs, self.model)

        # Inicializa o mecanismo de busca (retriever) com os embeddings e textos
        self.retriever = Retriever(self.embeddings, self.docs, top_k=top_k)

        # Cria uma pipeline de Pergunta e Resposta com um modelo da Hugging Face
        self.qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

    # Função para responder a uma pergunta usando os componentes anteriores
    def answer(self, question):
        # Gera embedding para a pergunta e busca os textos mais relevantes
        results = self.retriever.query(self.model.encode(question))

        # Usa apenas o primeiro resultado como contexto (poderia usar vários concatenados)
        context = results[0]

        # Usa a pipeline para gerar uma resposta com base na pergunta e contexto
        output = self.qa_pipeline(question=question, context=context)

        # Retorna apenas a resposta extraída
        return output["answer"]
