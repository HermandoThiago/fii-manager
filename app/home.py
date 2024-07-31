import streamlit as st
import plotly.express as px

from database.buy import purchases_group_fii_quantity

st.header('Carteira de fundos imobiliários')

st.markdown("<br>", unsafe_allow_html=True)

# Get data from the database
df = purchases_group_fii_quantity()

# Create the pie chart using Plotly
fig = px.pie(df, names='fundo', values='total_cotas', title='Total de cotas por FII')

# Display the pie chart in Streamlit
st.plotly_chart(fig)