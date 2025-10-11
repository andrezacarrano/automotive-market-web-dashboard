# 🚗 Car Sales Dashboard

Este é um aplicativo interativo desenvolvido com [Streamlit](https://streamlit.io/) para explorar dados de anúncios de carros usados nos Estados Unidos. Ele permite visualizar distribuições e relações entre variáveis como quilometragem, preço, ano do modelo, tipo de combustível, entre outros.

---

## 📊 Funcionalidades

- Histograma da quilometragem dos veículos (`odometer`)
- Gráfico de dispersão entre quilometragem e preço (`odometer` vs `price`)
- Interface interativa com botões e caixas de seleção
- Deploy na nuvem via [Render](https://render.com)

---

## 💻 Como executar localmente

1. Clone o repositório:

```bash
git clone https://github.com/andrezacarrano/car-sales-dashboard.git
cd car-sales-dashboard

---

## Deploy no Render

Este projeto está configurado para deploy automático no Render. Certifique-se de que os seguintes arquivos estão presentes:

app.py — código principal do app
requirements.txt — dependências
.streamlit/config.toml — configuração de porta para o Render

# Exemplo de config.toml:

[server]
headless = true
port = 10000

[browser]
serverAddress = "0.0.0.0"
serverPort = 10000
#Comando de inicialização no Render:
streamlit run app.py

---

##Estrutura do projeto
car-sales-dashboard/
├── app.py
├── vehicles_us.csv
├── requirements.txt
├── .streamlit/
│   └── config.toml
├── notebooks/
│   └── EDA.ipynb
└── README.md

---

##Requisitos
Python 3.8+
Streamlit
Pandas
Plotly

---

##Fonte dos dados
O conjunto de dados vehicles_us_csv contém informações sobre anúncios de carros usados nos EUA, incluindo preço, ano, modelo, tipo de combustível, quilometragem, entre outros.

---

##Demonstração
Acesse o app online:
 https://car-sales-dashboard-iauy.onrender.com/

---

Autora
Andreza Carrano
https://github.com/andrezacarrano