import streamlit as st

from database.buy import all_purchases

st.header("Registro de compras")

st.markdown("<br>", unsafe_allow_html=True)

st.table(all_purchases())
