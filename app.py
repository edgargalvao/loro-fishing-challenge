import streamlit as st
from src.qa_engine import QASystem

st.title("🎣 Loro Pesca — Assistente de Produtos")
qa = QASystem("data/loro_pesca_catalog.csv", "data/loro_pesca_technical_docs.csv")

question = st.text_input("Faça uma pergunta sobre um produto:")

if question:
    answer = qa.answer(question)
    st.write("**Resposta:**", answer)
