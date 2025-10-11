import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Análise de anúncios de carros usados')
df = pd.read_csv('vehicles_us.csv', sep='\t')
df.head()

if st.button('Criar histograma'):
    st.write('Histograma da coluna odômetro')
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

if st.button('Criar gráfico de dispersão'):
    st.write('Dispersão entre odômetro e preço')
    fig = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)
