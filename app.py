import pandas as pd
import plotly.express as px
import streamlit as st

# Cabeçalho do app
st.header("🚗 Dashboard de anúncios de vendas de carros")

# Lendo os dados com separador correto
car_data = pd.read_csv('vehicles_us.csv', sep='\t')

# Caixa de seleção para histograma
build_histogram = st.checkbox('📊 Criar um histograma')

if build_histogram:
    st.write('Criando um histograma para a coluna odometer')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Caixa de seleção para gráfico de dispersão
build_scatter = st.checkbox('📈 Criar gráfico de dispersão')

if build_scatter:
    st.write('Criando gráfico de dispersão entre odômetro e preço')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
