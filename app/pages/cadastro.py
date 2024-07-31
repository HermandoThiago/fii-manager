import streamlit as st
import pandas as pd

from database.buy import buy_fii

st.header("Cadastro de fiis")

st.markdown("<br>", unsafe_allow_html=True)

fiis = pd.read_csv('./app/database/fiis.csv')

fii = st.selectbox(
    'Selecione o fundo', 
    fiis['Fundos'].apply(lambda x: f"{x}.SA"),
    placeholder="Selecione o fii",
)

buy_date = st.date_input("Data de compra", value=None)

quantity = st.number_input("Quantidade", min_value=1, max_value=255, step=1, value=1)

value = st.number_input("Valor", step=1., format="%.2f")

submit_button = st.button("Inserir na carteira")

if submit_button:
  if fii and buy_date and quantity and value:
    try:
      buy_fii(fii, quantity, buy_date, value)

      st.success('Compra registrada com sucesso!', icon="✅")
    except:
      st.error('Ocorreu um erro ao cadastrar a compra!', icon="🚨")