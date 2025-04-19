# 🐟 Loro Pesca Q&A System

Sistema de Perguntas e Respostas baseado em documentos para a distribuidora fictícia **Loro Pesca**. Permite consultar informações sobre produtos (preço, disponibilidade, características técnicas) utilizando linguagem natural.

---

## 🧠 Arquitetura da Solução

A arquitetura adotada segue o padrão **Embedding + Similaridade Semântica**:

1. **Pré-processamento**:
   - Os dados de catálogo e especificações técnicas são fundidos em um único texto por produto.
   - É feita uma correspondência *fuzzy* entre o nome do produto no catálogo (`product_name`) e o grupo de produto técnico (`product_group`), permitindo ligar, por exemplo, `"CARRETILHA VIZEL AIR 731"` com `"CARRETILHA VIZEL AIR"`.

2. **Geração de Embeddings**:
   - Utiliza o modelo `all-MiniLM-L6-v2` da `sentence-transformers` para transformar textos em vetores semânticos.

3. **Recuperação**:
   - Um índice `NearestNeighbors` com métrica de cosseno encontra o documento mais similar à pergunta feita.
   - O sistema retorna o parágrafo de produto mais relevante como resposta.

---

## ⚙️ Instalação e Execução

### ✅ Requisitos

- Python 3.8+
- pip

### 📦 Instale as dependências:

```bash
pip install -r requirements.txt
