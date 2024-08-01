import streamlit as st
import plotly.express as px

from database.buy import purchases_group_fii_quantity, purchases_group_fii_value

st.header('Carteira de fundos imobiliários')

st.markdown("<br>", unsafe_allow_html=True)

# Get data from the database
grouped_quantity = purchases_group_fii_quantity()
grouped_value = purchases_group_fii_value()

# Create the pie chart for total cotas using Plotly
fig_quantity = px.pie(grouped_quantity, names='fundo', values='total_cotas', title='Total de cotas por FII', 
             labels={'total_cotas': 'Total de Cotas'}, 
             hole=0.3)

# Update the chart to show the values as labels
fig_quantity.update_traces(textinfo='label+value')

# Create the pie chart for total valor using Plotly
fig_value = px.pie(grouped_value, names='fundo', values='total_valor', title='Valor total por FII', 
             labels={'total_valor': 'Valor total'}, 
             hole=0.3)

# Update the chart to show the values as labels
fig_value.update_traces(textinfo='label+value')

st.plotly_chart(fig_quantity)
st.plotly_chart(fig_value)
