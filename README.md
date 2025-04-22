# 🐟 Loro Fishing Challenge - Sistema de Perguntas e Respostas

Este repositório implementa um sistema leve de **perguntas e respostas (Q&A)** para o catálogo de produtos da fictícia empresa **Loro Pesca**. Ele utiliza embeddings de linguagem e busca por similaridade para encontrar, entre os documentos, a resposta mais relevante a uma pergunta do usuário.

---

## Visão Geral

- Carrega dados tabulares (`CSV`) com produtos e suas especificações técnicas.
- Usa `SentenceTransformer` para gerar embeddings semânticos.
- Utiliza `KNN` com distância cosseno para buscar documentos similares.
- Permite responder perguntas com base no catálogo e nas especificações técnicas.

---
## Decisões de Arquitetura
### Criação de documentos com merge por substring
- Juntar `'loro_pesca_catalog.csv'` com `'loro_pesca_techinical_docs.csv'` via substring entre `'product_name'` e `'product_group'`.
- Heurística simples e eficaz para associação entre produtos e especificações.

### `'all-MiniLM-L6-v2'` da `sentence-transformers`
- Modelo leve, rápido e eficiente para geração de embeddings sem a necessidade de GPUs.
- Foi considerado modelos como Ollama, porém não consegui gerar uma key da OpenAI.

### `'sklearn.neighbors-NearestNeighbors'` com métrica cosseno
- Implementação simples e eficaz para projetos pequenos com poucos documentos
- 
### Resposta com LLM
- Passa a pergunta e o documento recuperado para o modelo `'deepset/roberta-base-squad2'` via o pipeline da `'Hugging Face'`.
- Retorna a resposta extraída do trecho do documento.


### Separação modular por responsabilidade
- Dividir sistema em módulos (`'data_loader'`,`'embedder'`,`'retriever'`,`'qa_engine'` e `'app.py'`)
### Interface Streamlit
- Facilitar uso

## Instalação

```bash
git clone https://github.com/edgargalvao/loro-fishing-challenge.git
cd loro-fishing-challenge
pip install -r requirements.txt
```

---

## Estrutura

```
loro-fishing-challenge/
│
├── src/
│   ├── data_loader.py     		# Carregamento e junção de dados
│   ├── embedder.py        		# Modelo e geração de embeddings
│   ├── retriever.py       		# Busca de documentos por similaridade
│   └── qa_engine.py       		# Classe principal do sistema Q&A
├── data/
│   ├── loro_pesca_catalog.csv		# Produtos, preços e disponibiliade	
│   └── loro_pesca_technical_docs.csv	# Produtos e detalhes técnicos
└── app.py				# Interface Streamlit

```

---

## Documentação dos Módulos

### `data_loader.py`

```python
load_data(product_path, specs_path)
```
- Lê os CSVs dos produtos e especificações.

```python
merge_data(products, specs)
```
- Cria documentos combinando o nome, código, preço, disponibilidade e especificações técnicas.

---

### `embedder.py`

```python
get_model()
```
- Carrega o modelo `'all-MiniLM-L6-v2'` da `sentence-transformers`.

```python
embed_texts(texts, model)
```
- Converte textos em vetores de embeddings.

---

### `retriever.py`

```python
Retriever(embeddings, texts)
```
- Inicializa a busca com KNN e distância cosseno.

```python
query(embedding)
```
- Retorna o documento mais similar ao embedding da pergunta.

---

### `qa_engine.py`

```python
QASystem(product_path, specs_path)
```
- Carrega os dados, cria os documentos, gera embeddings e indexa tudo.

```python
answer(question)
```
- Retorna a resposta mais relevante com base na pergunta do usuário.

---

## Exemplo de Uso

```bash
streamlit run app.py
```

---

## Modelo Utilizado

- [`sentence-transformers/all-MiniLM-L6-v2`](https://www.sbert.net/docs/pretrained_models.html)
  - Leve, eficiente e ideal para tarefas de busca semântica.

---
## Considerações finais
- O sistema funciona bem para palavras chaves como: "Disponível", "Indisponível", etc. Pois ele interpreta as palvras dadas no dataset.
- O sistema não funiciona muito bem para palavras subjetivas como: "Mais caro", "Mais barato".
- A maior dificuldade foi em tentar encontrar o modelo ideal para o projeto. Em Sentence Transformers temos varios modelos, mas após experimentos com modelos muito maiores, com desempenho não muito superior.
- Outra grande dificuldade foi tentar implementar com OpenAI. Não fui capaz de rodar Ollama, devido a necessidade da chave de acesso.
---
