import pandas as pd
import plotly.express as px
import streamlit as st

# Carregar os dados
df = pd.read_csv('vehicles_us.csv', sep='\t')

# Título
st.title("🚗 Car Sales Dashboard")

st.markdown("""
Explore os dados de anúncios de carros usados nos EUA.  
Escolha as variáveis para os eixos X e Y e visualize os gráficos interativos.
""")

st.markdown("---")

# Lista de colunas numéricas para os gráficos
numeric_cols = df.select_dtypes(include='number').columns.tolist()

# Seleção de eixos
x_axis = st.selectbox("📌 Escolha o eixo X", options=numeric_cols, index=numeric_cols.index(
    'odometer') if 'odometer' in numeric_cols else 0)
y_axis = st.selectbox("📌 Escolha o eixo Y", options=numeric_cols,
                      index=numeric_cols.index('price') if 'price' in numeric_cols else 1)

st.markdown("---")

# Botões para gerar gráficos
if st.button("📊 Gerar histograma do eixo X"):
    fig_hist = px.histogram(df, x=x_axis, nbins=50,
                            title=f"Distribuição de {x_axis}")
    st.plotly_chart(fig_hist, use_container_width=True)

if st.button("📈 Gerar gráfico de dispersão"):
    fig_scatter = px.scatter(df, x=x_axis, y=y_axis,
                             title=f"{x_axis} vs {y_axis}")
    st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("---")
st.markdown(
    "Desenvolvido por **Andreza Carrano** | [GitHub](https://github.com/andrezacarrano)")
